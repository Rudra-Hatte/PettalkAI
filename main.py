from flask import Flask, request, jsonify
from flask_cors import CORS

# Import your model or model helper functions here
# from model import pet_to_human, human_to_pet

app = Flask(__name__)
CORS(app)  # Enable CORS if you're connecting from a frontend

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to PettalkAI Backend!'})

@app.route('/translate/pet-to-human', methods=['POST'])
def translate_pet_to_human():
    data = request.json
    pet_message = data.get('pet_message', '')
    if not pet_message:
        return jsonify({'error': 'pet_message is required'}), 400

    # Placeholder: Replace this with your model inference
    # human_translation = pet_to_human(pet_message)
    human_translation = f"Translated pet message: {pet_message}"  # Dummy

    return jsonify({'human_message': human_translation})

@app.route('/translate/human-to-pet', methods=['POST'])
def translate_human_to_pet():
    data = request.json
    human_message = data.get('human_message', '')
    if not human_message:
        return jsonify({'error': 'human_message is required'}), 400

    # Placeholder: Replace this with your model inference
    # pet_translation = human_to_pet(human_message)
    pet_translation = f"Translated human message: {human_message}"  # Dummy

    return jsonify({'pet_message': pet_translation})

if __name__ == '__main__':
    app.run(debug=True)