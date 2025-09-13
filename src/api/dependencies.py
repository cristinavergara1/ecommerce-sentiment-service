from fastapi import Depends
from transformers import pipeline

def get_sentiment_model():
    model = pipeline("sentiment-analysis", model="AventIQ-AI/XLMRoBERTa_Multilingual_Sentiment_Analysis")
    return model

def get_model_dependency():
    return Depends(get_sentiment_model)