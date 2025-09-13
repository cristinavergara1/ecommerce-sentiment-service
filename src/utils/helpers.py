def preprocess_text(text: str) -> str:
    # Implementa la lógica para limpiar y preprocesar el texto
    return text.strip().lower()

def format_response(sentiment: str, score: float) -> dict:
    return {
        "sentiment": sentiment,
        "score": score
    }