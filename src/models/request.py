from pydantic import BaseModel
from typing import List, Optional

class SentimentRequest(BaseModel):
    text: str
    language: Optional[str] = None

class BatchSentimentRequest(BaseModel):
    texts: List[str]
    language: Optional[str] = None