from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from typing import Dict, List

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {}
user_chats = {}

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class ChatRecord(BaseModel):
    question: str
    answer: str

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/signup")
def signup(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="이미 존재하는 사용자명입니다.")
    fake_users_db[user.username] = {
        "email": user.email,
        "hashed_password": get_password_hash(user.password)
    }
    user_chats[user.username] = []
    return {"message": "회원가입이 완료되었습니다."}

@router.post("/login")
def login(user: UserLogin):
    db_user = fake_users_db.get(user.username)
    if not db_user:
        raise HTTPException(status_code=400, detail="존재하지 않는 사용자입니다.")
    if not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=400, detail="비밀번호가 일치하지 않습니다.")
    return {"message": "로그인 성공", "username": user.username}

@router.post("/chat/{username}")
def chat(username: str, chat: ChatRecord):
    if username not in user_chats:
        raise HTTPException(status_code=404, detail="유저가 존재하지 않습니다.")
    user_chats[username].append({"question": chat.question, "answer": chat.answer})
    return {"message": "채팅 기록 저장 완료"}

@router.get("/chat/{username}", response_model=List[ChatRecord])
def get_chat_history(username: str):
    if username not in user_chats:
        raise HTTPException(status_code=404, detail="유저가 존재하지 않습니다.")
    return user_chats[username]
