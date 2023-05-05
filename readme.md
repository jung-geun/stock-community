# fastapi와 svelte를 이용한 웹페이지 구현
## 1. 개발환경
[backend]
- python 3.10.11
- fastapi 0.95.1
- uvicorn 0.22.0
[frontend]
- svelte 4.3.3
## 2. 주석
- [x] 주석은 한글로 작성한다.
- [x] 주석은 """ """을 사용한다.
## 3. 배포 방법
- [x] backend
    - [x] dockerfile을 이용한 배포 - 추후 작성 예정
- [x] frontend
    - [x] npm run build
    - [x] dockerfile을 이용한 배포 - 추후 작성 예정

## 4. 코드
- [x] backend
    - [x] fastapi를 이용한 api 구현
        
- [x] frontend
    - [x] svelte를 이용한 웹페이지 구현
    - [x] sveltekit을 이용한 라우팅 구현 예정
    - [x] sveltekit을 이용한 api 호출 구현 예정

## 5. 사용 방법
- [x] backend 테스트
    - [x] backend 폴더에서 다음 명령어를 실행
    ```bash
    npm run dev
    ```
    - [x] fastapi 실행
    ```bash
    uvicorn api:app --port 8000 --reload
    ```
    - [x] http://localhost:8000/docs 에서 api 확인

- [x] database 연결
    - [x] .db.example.json 을 db.json 으로 변경하여 사용
    - [x] db.json은 gitignore에 등록되어 있음
    - [x] db.json은 backend 폴더에 위치
    - [x] db.json은 다음과 같은 형식으로 작성
    ```json
    {
        "dialect":"mysql",
        "driver": "pymysql",
        "user":"root",
        "password":"root",
        "host":"192.168.0.100",
        "port":3306,
        "database" : "database"
    }
    ```
    - [x] database 의 설정값을 환경에 맞게 변경

