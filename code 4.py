import speech_recognition as sr
from googletrans import Translator
import threading

recognizer = sr.Recognizer()
translator = Translator()


def transcribe_and_translate():
    with sr.Microphone() as source:
        print("Listening for audio...")

        while True:
            try:
                
                recognizer.energy_threshold = 4000  
                recognizer.pause_threshold = 0.8  

                audio_data = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio_data, language="en-IN")
                print(f"Transcription: {text}")

                
                translation = translator.translate(text, src="auto", dest="en").text
                print(f"Translation: {translation}")
            except sr.WaitTimeoutError:
                print("Listening timeout. No speech detected.")
            except sr.UnknownValueError:
                print("Could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

if __name__ == "__main__":
    
    transcribe_and_translate_thread = threading.Thread(target=transcribe_and_translate)
    transcribe_and_translate_thread.daemon = True
    transcribe_and_translate_thread.start()

    transcribe_and_translate_thread.join()  
