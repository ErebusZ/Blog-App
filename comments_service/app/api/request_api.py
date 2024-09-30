import os

from fastapi import Depends, HTTPException
from fastapi import HTTPAuthorizationCredentials, HTTPBearer
import httpx


AUTH_SERVICE_URL = (
    f"{os.environ.get('AUTH_HOST', 'https://auth-service.com/validate_token')}"
)


security = HTTPBearer()


async def validate_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    async with httpx.AsyncClient() as client:
        response = await client.post(DJANGO_BACKEND_URL, json={"token": token})
        if response.status_code == 200:
            data = response.json()
            if data["valid"]:
                return data
        raise HTTPException(status_code=401, detail="Invalid token")
