from fastapi import FastAPI
from .api.routes.sentiment import router as sentiment_router
from .core.logging import configure_logging

app = FastAPI(title="Sentiment Analysis Microservice")

configure_logging()

app.include_router(sentiment_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis Microservice"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)