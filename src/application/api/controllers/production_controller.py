from src.application.api.controllers import controller


@controller.post('/api/production/add_order', tags=["production"])
async def add_order():
    pass