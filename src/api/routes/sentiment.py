from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.sentiment_service import analyze_sentiment

router = APIRouter()

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    score: float

@router.post("/analyze", response_model=SentimentResponse)
async def analyze(request: SentimentRequest):
    try:
        result = analyze_sentiment(request.text)
        return SentimentResponse(label=result['label'], score=result['score'])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))