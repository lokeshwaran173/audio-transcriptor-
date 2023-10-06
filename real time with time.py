import speech_recognition as sr
from googletrans import Translator

# Function to transcribe audio for a specified duration of time
def transcribe_audio_by_time(duration_seconds):
    recognizer = sr.Recognizer()

    # Open the microphone and start recording for the specified duration
    with sr.Microphone() as source:
        print(f"Recording for {duration_seconds} seconds...")
        audio = recognizer.listen(source, timeout=duration_seconds)

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

# Specify the duration of audio capture in seconds
capture_duration_seconds = 30  # You can adjust this as needed

# Transcribe audio for the specified duration
transcription = transcribe_audio_by_time(capture_duration_seconds)

if transcription:
    print(f"Transcription: {transcription}")
    
    # Translate the transcription to English
    translation = translate_text(transcription)
    print(f"Translation: {translation}")
else:
    print("Transcription failed or empty.")
