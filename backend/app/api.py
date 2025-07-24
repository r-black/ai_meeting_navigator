from fastapi import APIRouter, UploadFile, File, HTTPException
from app.tasks import process_meeting_audio
import os
from uuid import uuid4

router = APIRouter()
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "/tmp")

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    audio_id = str(uuid4())
    path = os.path.join(UPLOAD_DIR, f"{audio_id}.wav")
    with open(path, "wb") as f:
        f.write(await file.read())

    process_meeting_audio.delay(audio_id)
    return {"id": audio_id, "status": "processing"}

@router.get("/status/{audio_id}")
def status(audio_id: str):
    summary_path = os.path.join(UPLOAD_DIR, f"{audio_id}.summary.txt")
    if os.path.exists(summary_path):
        return {"id": audio_id, "status": "ready"}
    return {"id": audio_id, "status": "processing"}

@router.get("/result/{audio_id}")
def result(audio_id: str):
    summary_path = os.path.join(UPLOAD_DIR, f"{audio_id}.summary.txt")
    if not os.path.exists(summary_path):
        raise HTTPException(status_code=404, detail="Summary not ready")
    with open(summary_path, "r") as f:
        content = f.read()
    return {"id": audio_id, "summary": content}