from os import error
from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from typing import Any, List

from starlette import responses
from config import settings
import schemas 
from crud import crudcar
from db import database
from api.keycloak import get_current_user

router = APIRouter()

@router.get("/me", response_model=schemas.msg.ResponseUniversal)
async def get_me(
    *,
    current_user: dict = Depends(get_current_user)
) -> Any:
    return {
        "data" : current_user
    }