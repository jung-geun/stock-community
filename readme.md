# fastapi와 svelte(feat. [vite](https://vitejs-kr.github.io/))를 이용한 웹페이지 구현

## 1. 개발환경

[backend]

- python 3.10.11
- fastapi 0.95.1
- uvicorn 0.22.0

[frontend]

- svelte 3.58.0
- vite 4.3.3

## 2. 주석

- [x] 주석은 한글로 작성한다.
- [x] 주석은 코드 상단에 """ """을 사용한다.

## 3. 파일 구조

```bash
.
├── backend
│   ├── .db_example.json
│   ├── api.py
│   ├── database.py
│   ├── db.json
│   ├── models.py
├── frontend
│   ├── public
│   │   └── favicon.ico
│   ├── src
│   │   ├── App.svelte
│   │   ├── components
│   │   │   ├── Footer.svelte
│   │   │   ├── Header.svelte
│   │   │   └── Nav.svelte
│   │   ├── main.js
│   │   ├── pages
│   │   │   ├── About.svelte
│   │   │   ├── Home.svelte
│   │   │   └── NotFound.svelte
│   │   └── routes.js
│   ├── .gitignore
│   ├── index.html
│   ├── jsconfig.json
│   ├── packege-lock.json
│   ├── package.json
│   ├── postcss.config.cjs
│   ├── README.md
│   ├── svelte.config.js
│   ├── tailwind.config.cjs
│   └── vite.config.js
├── .gitignore
└── README.md
```

## 4. 구현 방법

[x] backend

- fastapi를 이용한 api 구현

[x] frontend

- svelte를 이용한 웹페이지 구현
- vite를 이용한 빌드 및 실행

## 5. 사용 방법

[x] 패키지 설치

```bash
npm install 
```
package.json에 있는 패키지를 설치

[x] backend 테스트

- backend 폴더에서 다음 명령어를 실행

  ```bash
  npm run dev
  ```

- fastapi 실행

  ```bash
  uvicorn api:app --port 8000 --reload
  ```

  http://localhost:8000/docs 에서 api 확인 가능

[x] database 연결

- .db_example.json 을 db.json 으로 변경하여 사용
- db.json은 backend 폴더에 위치
- db.json은 다음과 같은 형식으로 작성

```json
{
  "dialect": "mysql",
  "driver": "pymysql",
  "user": "root",
  "password": "root",
  "host": "192.168.0.100",
  "port": 3306,
  "database": "database"
}
```

- database 의 설정값을 환경에 맞게 변경
