import speech_recognition as sr
from googletrans import Translator

# Function to transcribe audio
def transcribe_audio():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        transcription = recognizer.recognize_google(audio, language="en-IN")
        return transcription
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Function to translate text to English
def translate_text(text):
    translator = Translator()
    translated = translator.translate(text, src="auto", dest="en")
    return translated.text

# Transcribe live audio
transcription = transcribe_audio()

if transcription:
    print(f"Transcription: {transcription}")

    # Translate the transcription to English
    translation = translate_text(transcription)
    print(f"Translation: {translation}")
else:
    print("Transcription failed or empty.")
