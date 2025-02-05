
from src.infra.ioc.ioc import Ioc


class StartupApi:

    @staticmethod
    def initialize():
        Ioc.initialize()

        from fastapi import FastAPI
        app = FastAPI()

        from src.application.api.controllers import production_controller, health_check_controller

        app.include_router(health_check_controller.route)
        app.include_router(production_controller.route)

        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000, )