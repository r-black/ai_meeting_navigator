from app.services.config import USE_FASTER_WHISPER, TRITON_HOST
import requests

if USE_FASTER_WHISPER:
    from faster_whisper import WhisperModel
    model = WhisperModel(model_size_or_path="base", device="cpu", compute_type="int8")

def transcribe(path: str) -> str:
    if USE_FASTER_WHISPER:
        segments, _ = model.transcribe(path, language="ru")
        return " ".join([seg.text for seg in segments])
    else:
        with open(path, "rb") as f:
            response = requests.post(f"{TRITON_HOST}/transcribe", files={"audio_file": f})
        return response.json().get("text", "")
