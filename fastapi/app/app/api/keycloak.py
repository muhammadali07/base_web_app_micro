import logging
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, status, Security, Response
from fastapi.security import OAuth2AuthorizationCodeBearer

from pydantic import Json
from sqlalchemy import log
from config import settings
# Keycloak setup
from keycloak import KeycloakOpenID

keycloak_openid = KeycloakOpenID(
    server_url=settings.KEYCLOAK_AUTH_API,
    client_id=settings.KEYCLOAK_CLIENT,
    realm_name=settings.KEYCLOAK_REALM,
    client_secret_key=settings.KEYCLOAK_SECRET, # your backend client secret
    verify=False
)

app = FastAPI()

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="{0}realms/{1}/protocol/openid-connect/auth".format(settings.KEYCLOAK_AUTH_FRONT, settings.KEYCLOAK_REALM), 
    tokenUrl="{0}realms/{1}/protocol/openid-connect/token".format(settings.KEYCLOAK_AUTH_FRONT, settings.KEYCLOAK_REALM)
)


async def get_current_user(token: str = Depends(oauth2_scheme), response = Response):
    try:
        KEYCLOAK_PUBLIC_KEY = (
            "-----BEGIN PUBLIC KEY-----\n"
            + keycloak_openid.public_key()
            + "\n-----END PUBLIC KEY-----"
        )

        logging.info(keycloak_openid.public_key())
        return keycloak_openid.decode_token(
            token,
            key=KEYCLOAK_PUBLIC_KEY,
            options={"verify_signature": True, "verify_aud": False, "exp": True},
        )
    except Exception as e:
        logging.error(e)
        response.status_code=status.HTTP_401_UNAUTHORIZED
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )