# WBS 작성
---

## 1일차 - 프로젝트 준비 및 설계
### 프로젝트 주제 확정: 6월 제철음식 추천 서비스
### git 레포지토리 생성
### 와이어프레임 작성 ppt or 그림판
### WBS 작성

---

## 2일차 - 개발
###  FastAPI 환경 초기 설정

---

## 3일차 - 테스트
### 테스트 및 점검

```mermaid
gantt
    title 6월 제철 음식 추천 프로젝트 일정
    dateFormat  YYYY-MM-DD
    excludes    weekends

    section 기획
    요구사항 정의          :done,    req, 2025-06-10, 4h
    화면/기능 설계 구상    :done,    plan, after req, 4h

    section 프론트엔드 (HTML/CSS/JS)
    기본 UI 마크업 작성    :active,  ui, 2025-06-11, 4h
    버튼/결과 출력 구현    :         jslogic, after ui, 4h
    스타일링 (CSS)         :         style, after jslogic, 2h

    section 백엔드 (FastAPI)
    서버 구조 설정         :done,    fastapi-setup, 2025-06-10, 4h
    추천 로직 API 구현     :active,  api, 2025-06-11, 6h
    CORS 및 연동 처리      :         cors, after api, 2h

    section 통합 및 테스트
    프론트-백엔드 연동     :         connect, 2025-06-12, 4h
    디버깅 및 테스트       :         debug, after connect, 4h
    최종 점검 및 배포      :         deploy, after debug, 2h
```

## wireframe img
![wireframe](https://github.com/user-attachments/assets/24b84689-d0be-4549-9030-1a28982af4c0)