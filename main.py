from fastapi import FastAPI, HTTPException  # FastAPI 프레임워크와 예외처리
from pydantic import BaseModel  # 데이터 검증을 위한 모델 생성
import httpx  # HTTP 요청을 보내기 위한 라이브러리
from typing import List, Dict  # 타입 힌트를 위한 라이브러리
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:5500"],  # 프론트엔드 주소
    allow_origins=["*"],  # 수업에서는 모든 출처를 허용합니다.
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

