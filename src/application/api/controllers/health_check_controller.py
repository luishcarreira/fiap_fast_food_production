from src.application.api.controllers import controller_anonymous


@controller_anonymous.get('/api/healthcheck', tags=["heathcheck"])
async def healthcheck():
    return 'application is running 🚀'