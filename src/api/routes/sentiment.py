from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ...services.sentiment_service import analyze_sentiment
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/sentiment", tags=["sentiment"])

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    text: str
    results: list

@router.post("/analyze", response_model=SentimentResponse)
async def analyze_text_sentiment(request: SentimentRequest):
    try:
        logger.info(f"Analizando texto: {request.text[:100]}...")
        results = analyze_sentiment(request.text)
        logger.info(f"Resultados obtenidos: {results}")
        
        return SentimentResponse(text=request.text, results=results)
    except Exception as e:
        logger.error(f"Error en análisis de sentimiento: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "sentiment-analysis"}