from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.db.session import get_session, check_database_connection

route = APIRouter()

@route.get('/api/healthcheck', tags=["heathcheck"])
async def healthcheck(session: AsyncSession = Depends(get_session)):
    is_db_ok = await check_database_connection(session)

    if is_db_ok:
        return {"status": "ok", "message": "Application is running 🚀 and database ☁️ connection is healthy."}
    else:
        raise HTTPException(status_code=500, detail="Database connection failed.")