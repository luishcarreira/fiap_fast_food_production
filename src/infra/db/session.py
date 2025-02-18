import os
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

load_dotenv()

POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")

DATABASE_URL = (
    f"postgresql+asyncpg://{POSTGRES_USERNAME}:"
    f"{POSTGRES_PASSWORD}@{POSTGRES_HOST}:"
    f"{POSTGRES_PORT}/{POSTGRES_DATABASE}"
)

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency para o gerenciamento de sessões no FastAPI
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

async def check_database_connection(session: AsyncSession):
    try:
        from sqlalchemy import select
        result = await session.execute(select(1))
        if result.scalar() == 1:
            return True
        return False
    except Exception as e:
        print(f"Database connection error: {e}")
        return False