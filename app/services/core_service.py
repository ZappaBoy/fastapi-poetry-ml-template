from services.model.model import Model
from shared.utilities.configurator import Configurator
from shared.utilities.logger import Logger


class CoreService:
    def __init__(self):
        self.logger = Logger(self.__class__.__name__)

    def initialize(self):
        self.logger.info("Initializing core...")
        if Configurator.instance().get_settings().init_model:
            model = Model()
            model.initialize()
