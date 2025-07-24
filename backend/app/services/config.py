import os


UPLOAD_DIR = os.getenv("UPLOAD_DIR", "/tmp")
USE_FASTER_WHISPER = os.getenv("USE_FASTER_WHISPER", "true").lower() == "true"
