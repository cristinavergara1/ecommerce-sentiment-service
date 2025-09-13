from pydantic import BaseModel
from typing import List, Optional

class SentimentResponse(BaseModel):
    label: str
    score: float

class SentimentAnalysisResponse(BaseModel):
    sentiments: List[SentimentResponse]
    language: Optional[str] = None
    message: Optional[str] = None