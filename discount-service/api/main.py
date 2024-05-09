import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import discount

app = FastAPI()

# CORS 설정
origins = [
    "http://54.180.127.84/:3000",  # 허용할 프론트엔드 도메인
    "http://54.180.127.84/:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    #allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(discount.car_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8050, reload=True)
