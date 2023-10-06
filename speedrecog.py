import speech_recognition as sr
from googletrans import Translator

# Initialize the recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

def recognize_and_translate_speech_from_microphone():
    with sr.Microphone() as source:
        print("Listening for audio...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_sphinx(audio)
            print(f"Recognized: {text}")

            # Translate the transcription to English
            translation = translator.translate(text, src="auto", dest="en").text
            print(f"Translation: {translation}")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    recognize_and_translate_speech_from_microphone()
