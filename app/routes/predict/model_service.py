from typing import Any

from services.model.model import Model
from shared.utilities.logger import Logger


class ModelService:
    def __init__(self):
        self.logger = Logger(self.__class__.__name__)
        self.model = Model()

    def predict(self, data: Any):
        self.logger.info(f"Predicting...")
        result = self.model.predict(data)
        return {'result': result}
