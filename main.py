from flask import Flask, request, jsonify
from flask_cors import CORS

# Import your translation logic here (placeholder for now)
# from model import pet_to_human, human_to_pet

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (needed for frontend integration)

@app.route('/')
def home():
    return jsonify({'message': '🐾 Welcome to PetTalkAI Backend!'})

@app.route('/translate/pet-to-human', methods=['POST'])
def translate_pet_to_human():
    if not request.is_json:
        return jsonify({'error': 'Request must be in JSON format'}), 400

    data = request.get_json()
    pet_message = data.get('pet_message')

    if not pet_message:
        return jsonify({'error': 'pet_message is required'}), 400

    # Placeholder for model inference
    # human_translation = pet_to_human(pet_message)
    human_translation = f"Interpreted pet message: '{pet_message}'"  # Dummy response

    return jsonify({'human_message': human_translation}), 200

@app.route('/translate/human-to-pet', methods=['POST'])
def translate_human_to_pet():
    if not request.is_json:
        return jsonify({'error': 'Request must be in JSON format'}), 400

    data = request.get_json()
    human_message = data.get('human_message')

    if not human_message:
        return jsonify({'error': 'human_message is required'}), 400

    # Placeholder for model inference
    # pet_translation = human_to_pet(human_message)
    pet_translation = f"Converted to pet-speak: '{human_message}'"  # Dummy response

    return jsonify({'pet_message': pet_translation}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
