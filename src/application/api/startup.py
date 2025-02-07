from src.application.api.ioc.ioc import Ioc as IocApi


class Startup:

    @staticmethod
    def initialize():
        IocApi.initialize()

        from fastapi import FastAPI
        app = FastAPI()

        # app.add_middleware(
        #     CORSMiddleware,
        #     allow_origins=[
        #         "http://localhost",
        #         "http://localhost:3000",
        #     ],
        #     allow_credentials=True,
        #     allow_methods=["*"],
        #     allow_headers=["*"],
        # )

        from src.application.api.controllers import production_controller, health_check_controller

        app.include_router(health_check_controller.route)
        app.include_router(production_controller.route)

        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000, )