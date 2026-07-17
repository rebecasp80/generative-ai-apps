import torch
from transformers import pipeline

# Initialize the speech-to-text pipeline from Hugging Face Transformers
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=30,
)

# Path to the audio file
sample = "downloaded_audio.mp3"

# Transcribe
prediction = pipe(sample, batch_size=8)["text"]

print("Transcription:")
print(prediction)
