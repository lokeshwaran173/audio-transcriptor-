import speech_recognition as sr
from googletrans import Translator

# Function to translate text to English
def translate_text(text):
    translator = Translator()
    translated = translator.translate(text, src="auto", dest="en")
    return translated.text

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
microphone = sr.Microphone()

print("Listening...")

try:
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening to your voice... (Say something or press Ctrl+C to exit)")
        
        while True:
            try:
                audio = recognizer.listen(source, timeout=None)
                transcription = recognizer.recognize_google(audio, language="en-IN")
                print(f"Transcription: {transcription}")
                
                if transcription:
                    translation = translate_text(transcription)
                    print(f"Translation: {translation}")
                else:
                    print("No speech detected.")
            
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
except KeyboardInterrupt:
    print("Exited the program.")
