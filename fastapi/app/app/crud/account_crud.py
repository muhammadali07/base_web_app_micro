from datetime import datetime
import gevent
import uuid
from fastapi.logger import logger
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import update, or_, and_, insert, join, outerjoin, delete, func, desc, asc
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import (
    account_models
)

from app.utils import (
    ResponseOutCustom
)

from app.service import signJWT

from app.schemas import CreateAccoutuser

async def validasi_email_account(request:str, db_session:AsyncSession)-> ResponseOutCustom:
    async with db_session as session:
        tbusr = account_models.RequestUser
        get_data_user = select(tbusr.email).filter(tbusr.email == request)
        proxy_row = await session.execute(get_data_user)
        result = proxy_row.scalars().first()
        if result:
            return ResponseOutCustom(message_id="02", status="Failed, Email has been registed", list_data=[])
        else:
            return ResponseOutCustom(message_id="00", status="OK, Email already to registed", list_data=request)

async def create_account_user(request:CreateAccoutuser, db_session:AsyncSession) -> ResponseOutCustom:
    async with db_session as session:
        try:
            tbusr = account_models.RequestUser
            is_role = "AGENT" if request.role == 'T' else 'USER'
            new_user = tbusr(
                db_id = str(uuid.uuid4()),
                email = request.main.email,
                username = request.main.username,
                password = request.main.password,
                role = is_role
            )
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return ResponseOutCustom(message_id="00", status="Success", list_data=new_user)
        except gevent.Timeout:
            await session.invalidate()
            return ResponseOutCustom(
                message_id="02",
                status="Failed, DB transaction was timed out...",
                list_data=None,
            )

        except SQLAlchemyError as e:
            logger.error(e)
            await session.rollback()
            return ResponseOutCustom(
                message_id="02",
                status="Failed, something wrong rollback DB transaction...",
                list_data=None,
            )


async def auth_login(email:str, password:str, db_session:AsyncSession)->ResponseOutCustom:
    async with db_session as session:
        try:
            tbusr = account_models.RequestUser
            query_stmt = select(tbusr).filter(and_(tbusr.email == email, tbusr.password == password))
            proxy_row = await session.execute(query_stmt)
            result = proxy_row.scalars().first()
            data = jsonable_encoder(result)
            if (email == data['email']) and (password == data['password']):
                get_token = signJWT(
                    data['email'],
                    data['username'],
                    data['role']
                )
                return ResponseOutCustom(message_id="00", status="Success", list_data=get_token)
            else:
                return ResponseOutCustom(message_id="03", status="Failed Credentials Login", list_data=[])
        except gevent.Timeout:
            await session.invalidate()
            return ResponseOutCustom(
                message_id="02",
                status="Failed, DB transaction was timed out...",
                list_data=None,
            )

        except SQLAlchemyError as e:
            logger.error(e)
            await session.rollback()
            return ResponseOutCustom(
                message_id="02",
                status="Failed, something wrong rollback DB transaction...",
                list_data=None,
            )


async def get_list_user(db_session:AsyncSession)->ResponseOutCustom:
    async with db_session as session:
        try:
            tbusr = account_models.RequestUser
            query_stmt = (select(tbusr))
            proxy_row = await session.execute(query_stmt)
            result = proxy_row.scalars().all()
            list_data = jsonable_encoder(result)
            return ResponseOutCustom(message_id="00", status="Success", list_data=list_data)
        except gevent.Timeout:
            await session.invalidate()
            return ResponseOutCustom(
                message_id="02",
                status="Failed, DB transaction was timed out...",
                list_data=None,
            )

        except SQLAlchemyError as e:
            logger.error(e)
            await session.rollback()
            return ResponseOutCustom(
                message_id="02",
                status="Failed, something wrong rollback DB transaction...",
                list_data=None,
            )

