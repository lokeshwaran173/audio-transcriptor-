import speech_recognition as sr
from googletrans import Translator
from pydub import AudioSegment

# Function to convert audio to WAV format
def convert_audio(audio_file_path):
    audio = AudioSegment.from_file(audio_file_path, format="mp3")
    wav_path = audio_file_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")
    return wav_path

# Function to transcribe audio
def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
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

# Specify the path to your audio file
audio_file_path = 'C:/Users/lokes/Desktop/sih 1456/audio.wav'

# Convert audio to WAV format
wav_path = convert_audio(audio_file_path)

# Transcribe audio
transcription = transcribe_audio(wav_path)

if transcription:
    print(f"Transcription: {transcription}")
    
    # Translate the transcription to English
    translation = translate_text(transcription)
    print(f"Translation: {translation}")
else:
    print("Transcription failed or empty.")
