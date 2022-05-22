from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from app.config import settings
from sqlalchemy.orm import sessionmaker
import warnings
from sqlalchemy import exc as sa_exc

warnings.simplefilter("ignore", category=sa_exc.SAWarning)

# creates an instance of AsyncEngine which then offers an async version
engine = create_async_engine(
    settings.SQLALCHEMY_WITH_DRIVER_URI,
    echo=False, # set it to True if you wanna know what sqlalchemy did
    pool_size=100,
    max_overflow=200,
    pool_recycle=300,
    pool_pre_ping=True,
    pool_use_lifo=True)

# create AsyncSession sessionmaker version
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

metadata = MetaData()
Base = declarative_base(metadata=metadata)


# db async session
async def get_async_session():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()