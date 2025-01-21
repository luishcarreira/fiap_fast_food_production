import uvicorn
from fastapi import FastAPI

from src.infra.ioc.ioc import Ioc


class StartupApi:

    @staticmethod
    def initialize():
        Ioc.initialize()

        app = FastAPI()

        # routes
        from src.application.api.controllers import controller_anonymous, controller
        app.include_router(controller_anonymous)
        app.include_router(controller)

        uvicorn.run(app, host="0.0.0.0", port=8000, )