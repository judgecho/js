# JS_ver9 자동 채점 시스템 (백엔드 + 프론트엔드 통합)

## 실행 방법

1. Docker가 설치되어 있어야 합니다.
2. 터미널에서 아래 명령어 실행:

```
docker-compose up
```

- 프론트엔드: http://localhost:5173
- 백엔드: http://localhost:5001
- API 경로: http://localhost:5001/api/...

## 기능 요약

- 관리자 로그인 (역할: JS원장님, 부원장님, 선생님)
- 시험 목록 조회 및 복사 기능
- 반응형 Tailwind UI
- JWT 기반 인증 처리