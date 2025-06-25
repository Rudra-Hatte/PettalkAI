import logging
from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS
from typing import Optional, Dict

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# Modular translation logic
class PetTranslator:
    def __init__(self):
        # Initialize/load ML/NLP models here (placeholder)
        # self.pet_to_human_model = load_pet_to_human_model()
        # self.human_to_pet_model = load_human_to_pet_model()
        logging.info("PetTranslator initialized (dummy logic).")

    def pet_to_human(self, pet_message: str, species: str = "dog") -> str:
        # Placeholder: In reality, process with ML/NLP model based on species
        # Example: return self.pet_to_human_model.infer(pet_message, species)
        logging.info(f"Translating pet_to_human | species={species} | message='{pet_message}'")
        # Dummy logic:
        return f"[{species.capitalize()} says]: 'I'm happy and want to play!' (interpreted from '{pet_message}')"

    def human_to_pet(self, human_message: str, species: str = "dog") -> str:
        # Placeholder: In reality, process with ML/NLP model based on species
        # Example: return self.human_to_pet_model.infer(human_message, species)
        logging.info(f"Translating human_to_pet | species={species} | message='{human_message}'")
        # Dummy logic:
        return f"[Pet-speak for {species}]: 'Woof woof!' (translated from '{human_message}')"

# Flask Blueprint for translation routes
translation_bp = Blueprint('translation', __name__)
translator = PetTranslator()

@translation_bp.route('/translate/pet-to-human', methods=['POST'])
def translate_pet_to_human():
    if not request.is_json:
        return jsonify({'error': 'Request must be in JSON format'}), 400
    data = request.get_json()
    pet_message = data.get('pet_message')
    species = data.get('species', 'dog')
    if not pet_message:
        return jsonify({'error': 'pet_message is required'}), 400
    try:
        human_translation = translator.pet_to_human(pet_message, species)
        return jsonify({'human_message': human_translation}), 200
    except Exception as e:
        logging.error(f"pet_to_human failed: {e}")
        return jsonify({'error': 'Translation failed', 'details': str(e)}), 500

@translation_bp.route('/translate/human-to-pet', methods=['POST'])
def translate_human_to_pet():
    if not request.is_json:
        return jsonify({'error': 'Request must be in JSON format'}), 400
    data = request.get_json()
    human_message = data.get('human_message')
    species = data.get('species', 'dog')
    if not human_message:
        return jsonify({'error': 'human_message is required'}), 400
    try:
        pet_translation = translator.human_to_pet(human_message, species)
        return jsonify({'pet_message': pet_translation}), 200
    except Exception as e:
        logging.error(f"human_to_pet failed: {e}")
        return jsonify({'error': 'Translation failed', 'details': str(e)}), 500

# Core Flask app
app = Flask(__name__)
CORS(app)
app.register_blueprint(translation_bp)

@app.route('/')
def home():
    return jsonify({
        'message': '🐾 Welcome to PetTalkAI Backend!',
        'routes': [
            '/translate/pet-to-human [POST]',
            '/translate/human-to-pet [POST]'
        ]
    }), 200

# Error handlers for better API UX
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)