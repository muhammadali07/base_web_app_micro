from email.policy import HTTP
import logging
from fastapi import APIRouter, status, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_async_session
from app.utils import (
    handle_error_code
)

#model
from app.schemas import (
    RequestUser,
    CreateAccoutuser
)

#crud
from app.crud import (
    account_crud
)

from app.service import JWTBearer, get_user_token

router = APIRouter()

@router.post(
    '/create-user-account',
    status_code = status.HTTP_200_OK,
    summary = 'Created Account User'
)
async def create_user_accunt(
    response : Response,
    request : CreateAccoutuser,
    db_session: AsyncSession = Depends(get_async_session)
):
    out_resp = await account_crud.validasi_email_account(request=request.main.email, db_session=db_session)
    if out_resp.message_id == "00":
        out_response = await account_crud.create_account_user(request, db_session)
        handle_error_code(out_response, response)
        return out_response
    else:
        handle_error_code(out_resp, response)
        return out_resp

@router.get(
    '/validasi-user-account',
    status_code = status.HTTP_200_OK,
    summary = 'Validasi User Account'
    )
async def validasi_use_account(
    response:Response,
    email : str, 
    db_session:AsyncSession = Depends(get_async_session)
):
    out_response = await account_crud.validasi_email_account(email, db_session)
    handle_error_code(out_response,response)
    return out_response

@router.get(
    '/auth-login',
    status_code = status.HTTP_200_OK,
    summary = 'Auth Login'
)
async def auth_login(
    response : Response,
    email : str,
    password : str,
    db_session : AsyncSession= Depends(get_async_session),
    # user_info = [Depends(JWTBearer())]
):
    out_response = await account_crud.auth_login(email, password, db_session)
    handle_error_code(out_response, response)
    return out_response

@router.get(
    '/get-list-user',
    status_code = status.HTTP_200_OK,
    summary = 'Get List User'
    )
async def get_list_user(
    response : Response,
    db_session:AsyncSession=Depends(get_async_session),
    user_info: dict = Depends(get_user_token)
):
    logging.debug(user_info)
    out_response = await account_crud.get_list_user(db_session)
    handle_error_code(out_response, response)
    return out_response
