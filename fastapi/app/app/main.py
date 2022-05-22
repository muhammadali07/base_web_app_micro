import logging.config
import random
import string
from sys import prefix
import time

from .config import settings

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.logger import logger
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette.middleware.cors import CORSMiddleware

from app.api import api_router  
from app.db import engine, Base

# setup loggers
logging.config.fileConfig("/app/app/logging.conf", disable_existing_loggers=False)

s_logger = logging.getLogger(__name__)

app = FastAPI(
    title = settings.PROJECT_NAME,
    openapi_url = f"{settings.API_VERSION}/openapi.json",
)

app.mount('/api/v1/static', StaticFiles(directory = '/app/app/static'), name = 'static')

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    response = {
        "request_url": request.url,
        "response_code": f"{exc.status_code}",
        "response_msg": exc.detail,
        "message": exc.detail,
    }
    logger.warn(f"{response}")
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(response),
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(
        "start request",
        extra={
            "rid": idem,
            "path": request.url.path,
            "token": request.headers.get("Authorization"),
        },
    )

    start_time = time.time()
    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = "{0:.2f}".format(process_time)
    logger.info(
        "completed request",
        extra={
            "rid": idem,
            "path": request.url.path,
            "run_duration": formatted_process_time,
            "status_code": response.status_code,
        },
    )

    return response

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # DELETE ALL TABLE
        # await conn.run_sync(Base.metadata.drop_all)

        # CREATE ALL TABLE based on imported models
        await conn.run_sync(Base.metadata.create_all)
        # migration seed
        logger.info("Migration started...")
        # await user_seed.start(conn) # use from keycloak
        logger.info("Migration finished...")

@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(api_router, prefix=f"{settings.API_VERSION}")

logger.handlers = s_logger.handlers
logger.debug(settings)



@app.get("/url-list")
def get_all_ursl():
    url_list = [
        {"path": route.path, "name": route.name, "method": list(route.methods)[0]}
        for route in app.routes
    ]
    return url_list
