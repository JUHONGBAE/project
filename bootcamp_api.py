from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import httpx

router = APIRouter()

BOOTCAMP_API_URL = "https://dev.wenivops.co.kr/services/openai-api"

class Message(BaseModel):
    role: str
    content: str

class SimpleChatRequest(BaseModel):
    message: str
    system_message: str = "You are a helpful assistant."

class ConversationRequest(BaseModel):
    messages: List[Message]

class ChatResponse(BaseModel):
    response: str
    usage: Dict

@router.post("/chat/simple", response_model=ChatResponse)
async def simple_chat(request: SimpleChatRequest):
    messages = [
        {"role": "system", "content": request.system_message},
        {"role": "user", "content": request.message}
    ]
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                BOOTCAMP_API_URL,
                json=messages,
                timeout=30.0
            )
            response.raise_for_status()
            response_data = response.json()
            ai_message = response_data["choices"][0]["message"]["content"]
            usage_info = response_data["usage"]
            return ChatResponse(response=ai_message, usage=usage_info)
        except httpx.TimeoutException:
            raise HTTPException(status_code=408, detail="API 요청 시간이 초과되었습니다")
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f"API 오류: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"서버 오류: {str(e)}")

@router.post("/chat/conversation", response_model=ChatResponse)
async def conversation_chat(request: ConversationRequest):
    messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]
    if not any(msg["role"] == "system" for msg in messages):
        messages.insert(0, {"role": "system", "content": "You are a helpful assistant."})

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                BOOTCAMP_API_URL,
                json=messages,
                timeout=30.0
            )
            response.raise_for_status()
            response_data = response.json()
            ai_message = response_data["choices"][0]["message"]["content"]
            usage_info = response_data["usage"]
            return ChatResponse(response=ai_message, usage=usage_info)
        except httpx.TimeoutException:
            raise HTTPException(status_code=408, detail="API 요청 시간이 초과되었습니다")
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f"API 오류: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"서버 오류: {str(e)}")

@router.post("/chat/role")
async def role_based_chat(role: str, message: str):
    if role == "시인":
        system_message = "assistant는 시인이다. 모든 답변을 아름다운 시의 형태로 표현한다."
    elif role == "파이썬 선생님":
        system_message = "assistant는 친절한 파이썬 알고리즘의 힌트를 주는 선생님이다."
    elif role == "요리사":
        system_message = "assistant는 경험이 풍부한 요리사다. 맛있는 요리법을 알려준다."
    else:
        system_message = f"assistant는 {role}이다."

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": message}
    ]

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                BOOTCAMP_API_URL,
                json=messages,
                timeout=30.0
            )
            response.raise_for_status()
            response_data = response.json()
            return {
                "role": role,
                "user_message": message,
                "ai_response": response_data["choices"][0]["message"]["content"],
                "usage": response_data["usage"]
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

from fastapi import Request  # 이미 있다면 생략

@router.post("/recommend")
async def recommend(request: Request):
    body = await request.json()
    user_prompt = body.get("prompt", "6월 제철 음식 하나만 추천해줘")

    messages = [
        {"role": "system", "content": "당신은 음식 추천 전문가입니다. 계절에 맞는 요리를 간단하고 이해하기 쉽게 추천해주세요."},
        {"role": "user", "content": user_prompt}
    ]

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                BOOTCAMP_API_URL,
                json=messages,
                timeout=30.0
            )
            response.raise_for_status()
            response_data = response.json()
            ai_reply = response_data["choices"][0]["message"]["content"]
            usage_info = response_data["usage"]
            return {
                "prompt": user_prompt,
                "response": ai_reply,
                "usage": usage_info
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"추천 실패: {e}")
