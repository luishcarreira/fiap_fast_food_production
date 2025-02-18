import os
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_async_engine(os.getenv("DATABASE_URL"), echo=True)
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