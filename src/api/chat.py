import logging
from fastapi import APIRouter,HTTPException
from pydantic import BaseModel,Field

from src.agent.hr_agent import ask_hr_assistant

logger = logging.getLogger(__name__)
router=APIRouter()

class ChatRequest(BaseModel):
    question:str=Field(
        min_length=1,
        max_length=100,
        description="Question asked by the employee"
    )

class ChatResponse(BaseModel):
    answer: str

@router.post("/chat",response_model=ChatResponse)
def chat(request:ChatRequest):
    try:
        answer = ask_hr_assistant(request.question)

        return {"answer":answer}

    except Exception:
        logger.exception("Failed to process HR chat request")

        raise HTTPException(
            status_code=500,
            detail="Unable to process your question. Please try again later."
        )