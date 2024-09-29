import os

import requests
from fastapi import HTTPException, Request, status

AUTH_SERVICE_URL = f"{os.environ.get("AUTH_HOST", "https://auth-service.com/validate_token")}"


def validate_jwt(token: str) -> int:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(AUTH_SERVICE_URL, headers=headers)

    if response.status_code == 401:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    elif response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad request"
        )
    
    try:
        user_data = response.json()
        user_id = user_data.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User ID not found in response"
            )
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid response format from authentication service"
        )

    return user_id

def get_user_id(request: Request) -> int:
    authorization: str = request.headers.get("Authorization")
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing"
        )
    
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme"
            )
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header format"
        )

    return validate_jwt(token)
