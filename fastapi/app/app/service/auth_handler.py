import time
import jwt
import os
import logging
from decouple import config
from fastapi import HTTPException, Depends, status
from typing import Dict
from dotenv import load_dotenv
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from datetime import datetime

load_dotenv()

security = HTTPBearer()

# SECRET_JWT : str = b'b8ac372afc5f2d8dae3e4afcb07bc78837f74fbe6631621b'
# ALGORITH_JWT : str = "HS256"
# raise Exception(SECRET_JWT, ALGORITH_JWT)

JWT_SECRET : str = os.getenv('JWT_SECRET')
JWT_ALGORITHM : str = os.getenv('JWT_ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(user_id: str, username:str, role:str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "username": username,
        "role": role,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

def get_user_token(credentials: HTTPBasicCredentials = Depends(security)):
    token = credentials.credentials

    try:
        user_info = {}

        access_token_json = jwt.decode(token, options={"verify_signature": False})
        logging.debug(f'token result: {access_token_json}')

    except Exception as e:
        logging.error(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    #logging.debug(f'branch_code result: {request.branchCode}')

    if access_token_json.get('expires') < int(datetime.now().timestamp()):
        raise HTTPException(status_code=401, detail="Sesi login anda habis.")

    # user_info["user_id"] = access_token_json.get('preferred_username')
    user_info["username"] = access_token_json.get('username')
    user_info["role"] = access_token_json.get('role')
    # user_info["branch_code"] = access_token_json.get('branch_code', '001')  # default ke cabang 001 jika null
    # user_info["access_level"] = access_token_json.get('access_level', 1)  # default access level 1 jika null
    # user_info["divisi"] = access_token_json.get('divisi', 1)

    print(user_info)

    return user_info
