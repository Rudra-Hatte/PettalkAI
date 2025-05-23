from flask import Flask, request, jsonify
import speech_recognition as sr
import random
import os

app = Flask(__name__)

# Example "translation" map from barks to meanings
pet_intents = {
    "bark": [
        "I'm excited!",
        "Someone's at the door!",
        "Let's play!",
        "I need food."
    ],
    "meow": [
        "Feed me now!",
        "Where have you been?",
        "Pet me!",
        "I'm bored."
    ]
}

@app.route('/api/pet-talk', methods=['POST'])
def pet_talk():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400

    audio_file = request.files['audio']
    audio_path = os.path.join("temp_audio.wav")
    audio_file.save(audio_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        detected_word = recognizer.recognize_google(audio)
        print("Detected:", detected_word)
        if "bark" in detected_word.lower():
            reply = random.choice(pet_intents["bark"])
        elif "meow" in detected_word.lower():
            reply = random.choice(pet_intents["meow"])
        else:
            reply = "Hmm... I didn't understand that sound."
    except Exception as e:
        reply = f"Error processing audio: {str(e)}"

    os.remove(audio_path)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
