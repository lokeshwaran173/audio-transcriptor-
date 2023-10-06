import speech_recognition as sr
from googletrans import Translator


def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
    
    try:
        transcription = recognizer.recognize_google(audio_data, language="en-IN")
        return transcription
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


def translate_to_english(text):
    translator = Translator()
    
    try:
        translated_text = translator.translate(text, src="auto", dest="en").text
        return translated_text
    except Exception as e:
        print(f"Translation error: {e}")
        return None


audio_file_path = "audio.wav"


transcription = transcribe_audio(audio_file_path)

if transcription:
    print(f"Transcription: {transcription}")
    
    
    translation = translate_to_english(transcription)
    
    if translation:
        print(f"Translation: {translation}")
    else:
        print("Translation failed.")
else:
    print("Transcription failed.")
