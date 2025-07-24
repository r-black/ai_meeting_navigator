from app.services.config import USE_LLAMA_CPP, LLM_HOST, LLAMA_MODEL_PATH
import requests

# LLM backend: llama.cpp (CPU, локально)
if USE_LLAMA_CPP:
    from llama_cpp import Llama

    try:
        llm = Llama(
            model_path=LLAMA_MODEL_PATH,
            n_ctx=1024,
            n_threads=4,         # оптимально — количество логических ядер
            use_mlock=True,      # закрепить в RAM (без подкачки)
            verbose=False
        )
    except Exception as e:
        raise RuntimeError(f"Ошибка инициализации llama.cpp модели: {e}")

def summarize(text: str) -> str:
    try:
        if USE_LLAMA_CPP:
            prompt = f"Сделай краткое резюме следующего текста на русском языке:\n{text.strip()}\n"
            response = llm(
                prompt,
                max_tokens=512,
                temperature=0.2,
                top_p=0.9,
                stop=["\n"]
            )
            return response["choices"][0]["text"].strip()

        else:
            response = requests.post(
                f"{LLM_HOST}/v1/completions",
                json={
                    "prompt": f"Summarize this meeting:\n{text.strip()}",
                    "max_tokens": 512,
                    "temperature": 0.7
                },
                timeout=30
            )
            response.raise_for_status()
            return response.json().get("completion", "").strip()

    except Exception as e:
        return f"[LLM ERROR] {str(e)}"