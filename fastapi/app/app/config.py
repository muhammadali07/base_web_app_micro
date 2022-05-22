import secrets
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from pydantic import (
    BaseSettings,
    validator,
)
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
CONFIG_PATH = os.path.join(ROOT_DIR, 'gcp_storage_service_account.json')  # requires `import os`
# set environ variable to service account file. key path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CONFIG_PATH

# load .env from project
load_dotenv()


# BaseSettings get data from .env
class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv('PROJECT_NAME')
    API_VERSION: str = os.getenv('API_VERSION')
    PROXY_ROOT_PATH: str = os.getenv('PROXY_ROOT_PATH')
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEFAULT_PAGESIZE: int = 10
    POSTGRES_DB_SERVER: str = os.getenv('POSTGRES_DB_SERVER')
    POSTGRES_DB_API_USER: str = os.getenv('POSTGRES_DB_API_USER')
    POSTGRES_DB_API_PASSWORD: str = os.getenv('POSTGRES_DB_API_PASSWORD')
    POSTGRES_DB_API: str = os.getenv('POSTGRES_DB_API')

    # reactapp ENV
    KEYCLOAK_AUTH_FRONT: str =os.environ.get("KEYCLOAK_AUTH_FRONT")

    SQLALCHEMY_WITH_DRIVER_URI: Optional[str] = None

    @validator("SQLALCHEMY_WITH_DRIVER_URI", pre=True)
    def postgresql_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v

        # dialect[+driver]://user:password@host/dbname[?key=value..]
        scheme = "postgresql"
        driver = "asyncpg"
        user = values.get("POSTGRES_DB_API_USER")
        password = values.get("POSTGRES_DB_API_PASSWORD")
        host = values.get("POSTGRES_DB_SERVER")
        database = values.get("POSTGRES_DB_API")
        return "{}+{}://{}:{}@{}/{}".format(scheme, driver, user, password, host, database)

    # --

    ENVIRONMENT: str = 'dev'
    TESTING: bool = False

    POSTGRES_DB_SERVER_TEST: str = os.getenv('POSTGRES_DB_SERVER_TEST')
    POSTGRES_DB_API_USER_TEST: str = os.getenv('POSTGRES_DB_API_USER_TEST')
    POSTGRES_DB_API_PASSWORD_TEST: str = os.getenv('POSTGRES_DB_API_PASSWORD_TEST')
    POSTGRES_DB_API_TEST: str = os.getenv('POSTGRES_DB_API_TEST')
    SQLALCHEMY_WITH_DRIVER_URI_TEST: Optional[str] = None

    @validator("SQLALCHEMY_WITH_DRIVER_URI_TEST", pre=True)
    def postgresql_db_connection_test(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v

        # dialect[+driver]://user:password@host/dbname[?key=value..]
        scheme = "postgresql"
        driver = "asyncpg"
        user = values.get("POSTGRES_DB_API_USER_TEST")
        password = values.get("POSTGRES_DB_API_PASSWORD_TEST")
        host = values.get("POSTGRES_DB_SERVER_TEST")
        database = values.get("POSTGRES_DB_API_TEST")
        return "{}+{}://{}:{}@{}/{}".format(scheme, driver, user, password, host, database)

    # --

settings = Settings()
