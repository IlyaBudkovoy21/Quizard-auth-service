from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from src.vault import hvac_client


db_host = hvac_client.read_db_secret(key="host")
db_username = hvac_client.read_db_secret(key="username")
db_password = hvac_client.read_db_secret(key="password")
db_port = hvac_client.read_db_secret(key="port")
db_name = hvac_client.read_db_secret(key="database")


DATABASE_URL = (
    f"postgresql+asyncpg://{db_username}:{db_password}@"
    f"{db_host}:{db_port}/{db_name}"
)


db_engine = create_async_engine(DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(
    bind=db_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
