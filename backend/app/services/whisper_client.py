from app.services.config import USE_FASTER_WHISPER

if USE_FASTER_WHISPER:
    from faster_whisper import WhisperModel
    model = WhisperModel("base", compute_type="int8")  # можно поменять на "tiny", "small" и т.п.

def transcribe(path: str) -> str:
    segments, _ = model.transcribe(path, language="ru")
    return " ".join([seg.text for seg in segments])
