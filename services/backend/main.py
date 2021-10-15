import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings import ALLOWED_HOSTS
from routes.student import student_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(student_router, prefix='', tags=['students'])

if __name__ == '__main__':
    uvicorn.run(app, debug=True)
