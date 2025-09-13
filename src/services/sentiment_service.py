from transformers import pipeline
import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

class SentimentService:
    def __init__(self):
        try:
            logger.info("Cargando modelo de análisis de sentimientos...")
            self.model = pipeline(
                "sentiment-analysis", 
                model="AventIQ-AI/XLMRoBERTa_Multilingual_Sentiment_Analysis",
                return_all_scores=True
            )
            logger.info("Modelo cargado exitosamente")
        except Exception as e:
            logger.error(f"Error al cargar el modelo: {e}")
            raise
    
    def analyze(self, text: str) -> List[Dict[str, Any]]:
        try:
            results = self.model(text)
            return results[0] if results else []
        except Exception as e:
            logger.error(f"Error al analizar texto: {e}")
            raise

# Instancia global del servicio
_sentiment_service = None

def get_sentiment_service() -> SentimentService:
    global _sentiment_service
    if _sentiment_service is None:
        _sentiment_service = SentimentService()
    return _sentiment_service

def analyze_sentiment(text: str) -> List[Dict[str, Any]]:
    """
    Función para analizar el sentimiento de un texto.
    
    Args:
        text (str): Texto a analizar
        
    Returns:
        List[Dict[str, Any]]: Lista de resultados con etiquetas y puntuaciones
    """
    service = get_sentiment_service()
    return service.analyze(text)