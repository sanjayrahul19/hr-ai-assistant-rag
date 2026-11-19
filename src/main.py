from fastapi import FastAPI

from src.api.chat import router as chat_router

app = FastAPI(
    title="HR AI Assistant",
    description="AI-powered HR assistant using RAG and tool calling",
    version="1.0.0"
)

app.include_router(
    chat_router,
    prefix='/api',
    tags=["HR Assistant"]
)

@app.get("/")
def home():
     return {
        "message": "HR AI Assistant API is running"
    }
