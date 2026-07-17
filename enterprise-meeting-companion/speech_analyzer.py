import os
from dotenv import load_dotenv
from groq import Groq
from faster_whisper import WhisperModel
import gradio as gr

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

# -----------------------------
# Load Whisper model
# -----------------------------
whisper_model = WhisperModel("small", device="cpu", compute_type="int8")


# -----------------------------
# Transcription function
# -----------------------------
def transcribe_audio(audio_file):
    segments, info = whisper_model.transcribe(audio_file, beam_size=5)
    transcription = ""

    for segment in segments:
        transcription += segment.text + " "

    return transcription.strip()


# -----------------------------
# LLM analysis function
# -----------------------------
def analyze_text(text):
    prompt = f"""
You are an AI assistant specialized in analyzing business meetings.

Given the following meeting transcription, produce:

1. A concise summary (5–7 lines)
2. Key discussion points (bullet list)
3. Decisions made (bullet list)
4. Action items with responsible roles (bullet list)
5. Risks or concerns mentioned
6. Overall tone of the meeting (e.g., collaborative, tense, productive)
7. Opportunities identified

Meeting transcription:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# -----------------------------
# Main pipeline
# -----------------------------
def process_meeting(audio_file):
    if audio_file is None:
        return "Please upload an audio file."

    transcription = transcribe_audio(audio_file)
    analysis = analyze_text(transcription)

    return f"### 📝 Transcription\n{transcription}\n\n### 📊 Analysis\n{analysis}"


# -----------------------------
# Gradio Interface
# -----------------------------
app = gr.Interface(
    fn=process_meeting,
    inputs=gr.Audio(type="filepath", label="Upload meeting audio"),
    outputs=gr.Markdown(),
    title="Enterprise Meeting Analyzer",
    description="Upload an audio file from a meeting and receive a full AI-powered analysis."
)

# -----------------------------
# Launch app
# -----------------------------
if __name__ == "__main__":
    app.launch()
