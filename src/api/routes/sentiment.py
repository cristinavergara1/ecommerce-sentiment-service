from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ...services.sentiment_service import analyze_sentiment
from ...models.response import SentimentResponse, SentimentScore
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/sentiment", tags=["sentiment"])

class SentimentRequest(BaseModel):
    text: str

@router.post("/analyze", response_model=SentimentResponse)
async def analyze_text_sentiment(request: SentimentRequest):
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="El texto no puede estar vacío")
            
        logger.info(f"Analizando texto: {request.text[:100]}...")
        results = analyze_sentiment(request.text)
        logger.info(f"Resultados obtenidos: {results}")
        
        # Convertir all_scores a objetos SentimentScore
        sentiment_scores = [
            SentimentScore(**score) for score in results["all_scores"]
        ]
        
        return SentimentResponse(
            text=request.text,
            predicted_sentiment=results["predicted_sentiment"],
            confidence=results["confidence"],
            primary_score=results["primary_score"],
            all_scores=sentiment_scores
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en análisis de sentimiento: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "sentiment-analysis"}