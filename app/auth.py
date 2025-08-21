from fastapi import APIRouter, Request
from authlib.integrations.starlette_client import OAuth
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

oauth = OAuth()

oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
    timeout=300,
)


@router.get("/login")
async def login(request: Request):
    redirect_uri = os.getenv("GOOGLE_REDIRECT_URI")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/auth/google/callback")
async def callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    resp = await oauth.google.get(
        "https://openidconnect.googleapis.com/v1/userinfo", token=token
    )
    user_info = resp.json()
    return {"user": user_info, "token": token}
