from src.application.test.ioc import Ioc as IocTest


class Startup:

    @staticmethod
    def initialize():
        from fastapi import FastAPI
        from src.application.api.controllers import production_controller, health_check_controller

        app = FastAPI()

        # Configura as rotas para o modo de teste
        app.include_router(health_check_controller.route)
        app.include_router(production_controller.route)

        IocTest.initialize()

        return app