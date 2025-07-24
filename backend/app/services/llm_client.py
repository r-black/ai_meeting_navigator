from transformers import pipeline

summarizer = pipeline("summarization", model="philschmid/distilbart-cnn-6-6")

def summarize(text: str) -> str:
    try:
        if len(text.strip()) < 20:
            return "[LLM WARNING] Text too short to summarize"
        result = summarizer(text, max_length=128, min_length=32, do_sample=False)
        return result[0]["summary_text"]
    except Exception as e:
        return f"[LLM ERROR] {str(e)}"