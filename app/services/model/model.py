from typing import Any

from services.model.model_config import ModelConfig
from shared.utilities.logger import Logger


class Model:

    def __init__(self):
        self.logger = Logger(self.__class__.__name__)
        self.config = ModelConfig()

    def initialize(self):
        self.logger.info('Model initialization')
        # Here you can add the training method

    def predict(self, data: Any):
        return data
