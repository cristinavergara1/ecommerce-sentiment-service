from pydantic import BaseModel
from typing import List, Optional

class SentimentScore(BaseModel):
    label: str
    score: float
    confidence: str

class SentimentResponse(BaseModel):
    text: str
    predicted_sentiment: str
    confidence: str
    primary_score: float
    all_scores: List[SentimentScore]
    
class SentimentAnalysisResult(BaseModel):
    predicted_sentiment: str
    confidence: str
    primary_score: float
    all_scores: List[SentimentScore]