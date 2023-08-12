from typing import Any

from fastapi import Depends, Query
from fastapi.openapi.models import APIKey
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from routes.predict.model_service import ModelService
from shared.deps.api_key_auth import ApiKeyAuth
from shared.utilities.logger import Logger

router = InferringRouter()


@cbv(router)
class ModelController:
    api_key_auth = ApiKeyAuth()

    def __init__(self):
        self.logger = Logger(self.__class__.__name__)
        self.router = router
        self.predict_service = ModelService()

    @router.get("/predict")
    def predict(self, data: Any = Query(None),
                api_key: APIKey = Depends(api_key_auth.check_api_key)):
        return self.predict_service.predict(data)
