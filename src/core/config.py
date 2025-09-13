from pydantic import BaseSettings

class Settings(BaseSettings):
    huggingface_model: str = "AventIQ-AI/XLMRoBERTa_Multilingual_Sentiment_Analysis"
    api_key: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()