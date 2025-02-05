from fastapi import APIRouter

route = APIRouter()

@route.get('/api/healthcheck', tags=["heathcheck"])
async def healthcheck():
    return 'application is running 🚀'