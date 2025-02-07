from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from settings import get_settings

settings = get_settings()

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.postgresql_username}:"
    f"{settings.postgresql_password}@{settings.postgresql_host}:"
    f"{settings.postgresql_port}/{settings.postgresql_database}"
)

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Dependency para o gerenciamento de sessões no FastAPI
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
