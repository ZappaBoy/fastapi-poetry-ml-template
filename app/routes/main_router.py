from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from routes.predict.model_controller import ModelController
from shared.utilities.logger import Logger

router = APIRouter()


@cbv(router)
class MainRouter:
    def __init__(self):
        self.logger = Logger(self.__class__.__name__)
        self.router = router
        model_controller = ModelController()

        self.include(model_controller, prefix="/model")

    @staticmethod
    def include(external_router, **kwargs):
        router.include_router(external_router.router, **kwargs)

    @router.get("/health/check")
    def healthcheck(self):
        return {"detail": "alive"}
