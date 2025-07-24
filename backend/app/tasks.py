from app.celery_app import celery_app
from app.services.whisper_client import transcribe
from app.services.llm_client import summarize
import os


@celery_app.task
def process_meeting_audio(audio_id: str):
    path = os.path.join(os.getenv("UPLOAD_DIR", "/tmp"), f"{audio_id}.wav")
    text = transcribe(path)
    summary = summarize(text)
    with open(os.path.join(os.getenv("UPLOAD_DIR", "/tmp"), f"{audio_id}.summary.txt"), "w") as f:
        f.write(summary)