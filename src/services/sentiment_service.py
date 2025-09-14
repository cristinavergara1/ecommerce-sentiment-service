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
                top_k=None
            )
            logger.info("Modelo cargado exitosamente")
            
            # Mapeo de etiquetas del modelo a nombres descriptivos
            self.label_mapping = {
                "LABEL_0": "negative",
                "LABEL_1": "positive",
                "LABEL_2": "neutral"  # Si el modelo tiene 3 clases
            }
            
        except Exception as e:
            logger.error(f"Error al cargar el modelo: {e}")
            raise
    
    def _map_labels(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Mapea las etiquetas genéricas a nombres descriptivos y formatea la salida.
        """
        mapped_results = []
        
        for result in results:
            mapped_label = self.label_mapping.get(result['label'], result['label'])
            mapped_results.append({
                "label": mapped_label,
                "score": round(result['score'], 4),
                "confidence": "high" if result['score'] > 0.8 else "medium" if result['score'] > 0.6 else "low"
            })
        
        # Ordenar por score descendente
        mapped_results.sort(key=lambda x: x['score'], reverse=True)
        
        # Determinar el sentimiento predominante
        primary_sentiment = mapped_results[0] if mapped_results else {"label": "unknown", "score": 0.0, "confidence": "low"}
        
        return {
            "predicted_sentiment": primary_sentiment['label'],
            "confidence": primary_sentiment['confidence'],
            "primary_score": primary_sentiment['score'],
            "all_scores": mapped_results
        }
    
    def analyze(self, text: str) -> Dict[str, Any]:
        try:
            results = self.model(text)
            logger.info(f"Resultados raw del modelo: {results}")
            
            # Extraer la lista de resultados
            if isinstance(results, list) and len(results) > 0:
                if isinstance(results[0], list):
                    sentiment_results = results[0]
                else:
                    sentiment_results = results
            else:
                sentiment_results = []
            
            return self._map_labels(sentiment_results)
            
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

def analyze_sentiment(text: str) -> Dict[str, Any]:
    """
    Función para analizar el sentimiento de un texto.
    
    Args:
        text (str): Texto a analizar
        
    Returns:
        Dict[str, Any]: Resultados formateados con sentimiento predicho y puntuaciones
    """
    service = get_sentiment_service()
    return service.analyze(text)