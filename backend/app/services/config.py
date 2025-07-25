import os


UPLOAD_DIR = os.getenv("UPLOAD_DIR", "/tmp")
TRITON_HOST = os.getenv("TRITON_HOST", "http://triton:8000")
LLM_HOST = os.getenv("LLM_HOST", "http://llm:8000")
LLAMA_MODEL_PATH = os.getenv("LLAMA_MODEL_PATH", "/models/llama-1b.Q4_K_M.gguf")
USE_LLAMA_CPP = os.getenv("USE_LLAMA_CPP", "true").lower() == "true"
USE_FASTER_WHISPER = os.getenv("USE_FASTER_WHISPER", "true").lower() == "true"
