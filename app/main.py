# main.py
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from app.auth import router as auth_router

load_dotenv()

app = FastAPI()

# Session middleware
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

# CORS for frontend
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)


# from fastapi import FastAPI
# from starlette.middleware.sessions import SessionMiddleware
# from dotenv import load_dotenv
# from app.auth import router as auth_router
# import os

# load_dotenv()

# app = FastAPI()

# app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

# app.include_router(auth_router)
