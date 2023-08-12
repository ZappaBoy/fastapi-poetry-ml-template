from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from routes.predict.model_controller import ModelController
from shared.utilities.logger import Logger

router = InferringRouter()


@cbv(router)
class APIRouter:
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
        return {"Status": "Alive"}
