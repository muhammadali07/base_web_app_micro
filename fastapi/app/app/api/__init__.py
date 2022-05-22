from fastapi import APIRouter

from app.api import account


api_router = APIRouter()


#API
api_router.include_router(account.router, prefix='/account_user', tags=['Account Information'])
