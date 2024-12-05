from fastapi import HTTPException
from env import AUTH_TOKEN

def authenticate(token: str):
    if token != AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")