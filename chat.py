from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.services.ai_service import (
    chat_with_provider,
    chat_with_multiple_providers
)


router = APIRouter()


class ChatRequest(BaseModel):
    provider: str
    message: str


class MultiChatRequest(BaseModel):
    providers: list[str]
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):

    try:
        return await chat_with_provider(
            request.provider,
            request.message
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/multi-chat")
async def multi_chat(request: MultiChatRequest):

    try:
        return await chat_with_multiple_providers(
            request.message,
            request.providers
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )