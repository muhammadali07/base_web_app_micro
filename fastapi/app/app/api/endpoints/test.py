
from fastapi import APIRouter, Body, Depends, HTTPException
from typing import Any, List
from config import settings
router = APIRouter()

@router.get("/one")
async def testing_one_api(

)->Any:
    return {
        "response_code" : "00",
        "response_msg" : settings.SQLALCHEMY_DATABASE_URI
    }