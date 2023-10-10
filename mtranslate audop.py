import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

# Initialize the SpeechRecognition object
recognizer = sr.Recognizer()

# Function to transcribe and provide a corrected translation for an existing audio file
def transcribe_and_translate_audio(audio_file_path):
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)
            transcription_en = recognizer.recognize_google(audio_data, language="en-IN")
            transcription_hi = recognizer.recognize_google(audio_data, language="hi-IN")

            print(f"Transcription (English): {transcription_en}")
            print(f"Transcription (Hindi): {transcription_hi}")

            # Translate the English transcription to English using Google Translate API
            translator = Translator()
            translation = translator.translate(transcription_en, src="auto", dest="en")

            print(f"Translation (English): {translation.text}")

            # Convert the English translation to speech
            tts = gTTS(text=translation.text, lang='en')
            tts.save("translated_audio.mp3")

            # Play the translated audio using the playsound library
            playsound("translated_audio.mp3")

    except sr.UnknownValueError:
        print("No speech detected.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

# Specify the path to your existing audio file
audio_file_path = 'modijispeech.wav'

# Call the function to transcribe, translate, and play the English translation as audio in VS Code
transcribe_and_translate_audio(audio_file_path)
