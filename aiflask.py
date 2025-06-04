from flask import Flask, request, redirect, url_for, flash, session, jsonify,render_template
from google import genai
import speech_recognition as sr

from gtts import gTTS
import pygame


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['GET'])
def generate():
    user_input = request.args.get('msg', '')
    client = genai.Client(api_key="AIzaSyBvTIhZ0ZfUn8-gIAddFchtyx-tvB5YkGY")

    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=user_input,
    )
    
    return jsonify({'status': 'success', 'message': response.text})


@app.route('/voice', methods=['GET'])
def voice():
    language = int(request.args.get('lang', ''))
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice input...")
        audio_text = r.listen(source)
        print("Audio received, processing...")
        try:
            if language == 1:
                text = r.recognize_google(audio_text, language='en-US')
            elif language == 2:
                text = r.recognize_google(audio_text, language='my-MM')
            else:
                return jsonify({'status': 'error', 'message': 'Unsupported language'}), 400
            
            client = genai.Client(api_key="AIzaSyBvTIhZ0ZfUn8-gIAddFchtyx-tvB5YkGY")
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=text,
            )
            #voice
            pygame.mixer.init()
            sound_file = "sound_file.mp3"
            text_to_speech = gTTS(text=response.text, lang='my')
            text_to_speech.save(sound_file)
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
            while pygame.mixer.get_busy(): 
                pygame.time.delay(100)
            return jsonify({'status': 'success', 'message': response.text})
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return jsonify({'status': 'error', 'message': 'Could not understand audio'}), 400

    # return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)