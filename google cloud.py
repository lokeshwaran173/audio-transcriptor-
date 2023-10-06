from google.cloud import speech
from google.cloud import translate
from google.oauth2 import service_account
import os
import speech_recognition as sr
from googletrans import Translator
import pyaudio
import wave
import tempfile

# Set the path to your Google Cloud service account credentials JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/credentials.json"

# Function to transcribe audio using Google Cloud Speech-to-Text API
def transcribe_audio(audio_content):
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,  # Adjust this based on your audio
        language_code="en-IN",
    )

    response = client.recognize(config=config, audio=audio)

    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript

    return transcription

# Function to translate text to English
def translate_text(text):
    translator = Translator()
    translated = translator.translate(text, src="auto", dest="en")
    return translated.text

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Configure the audio stream
stream = audio.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=1024)

print("Listening...")

try:
    while True:
        audio_frames = []
        for i in range(0, int(16000 / 1024 * 20)):  # Adjust 20 seconds duration
            audio_data = stream.read(1024)
            audio_frames.append(audio_data)

        # Convert audio_frames to bytes
        audio_content = b"".join(audio_frames)

        transcription = transcribe_audio(audio_content)
        print(f"Transcription: {transcription}")

        if transcription:
            translation = translate_text(transcription)
            print(f"Translation: {translation}")
except KeyboardInterrupt:
    print("Exited the program.")
finally:
    # Clean up PyAudio and the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()
