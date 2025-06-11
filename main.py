from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth import router as auth_router
from bootcamp_api import router as bootcamp_router

app = FastAPI(title="통합 FastAPI 서버", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 운영 환경에 맞게 변경 필요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="")
app.include_router(bootcamp_router, prefix="")

@app.get("/")
async def root():
    return {"message": "통합 FastAPI 서버가 실행 중입니다."}



