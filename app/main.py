from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from .auth import router as auth_router
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

app.include_router(auth_router)
