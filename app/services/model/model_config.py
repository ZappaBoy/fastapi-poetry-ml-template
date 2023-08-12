import multiprocessing
import os
import random

import numpy as np
import tensorflow as tf
from tensorflow.python.framework.random_seed import set_random_seed

from config import GENERATED_RESOURCES_PATH
from shared.utilities.configurator import Configurator
from shared.utilities.logger import Logger
from shared.utilities.utilities import check_directory


class ModelConfig:
    resources_dir: str = os.path.join(GENERATED_RESOURCES_PATH, 'app')
    models_dir: str = os.path.join(resources_dir, 'models')
    dataset_dir: str = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'dataset')

    random_state = 1
    verbose_level = 1
    # https://rocmsoftwareplatform.github.io/MIOpen/doc/html/DebugAndLogging.html
    rocm_logging_level = -1

    use_all_threads = False
    num_threads = int(os.environ.get('NUM_THREADS', 16))
    # You can ignore the GPU if the model is too simple
    use_gpu = True
    limit_gpu_memory = True

    def __init__(self):
        self.logger = Logger(self.__class__.__name__)
        self.check_directories()
        self.initialize()

    def initialize(self):
        self.set_verbosity_level()
        self.set_threads_number()
        tf.config.set_soft_device_placement(True)
        self.set_seed(self.random_state)
        self.set_devices()
        if Configurator.instance().is_debug():
            tf.data.experimental.enable_debug_mode()
            self.set_verbosity_level(verbose_level=0, rocm_logging_level=7)
            self.print_envs()

    @staticmethod
    def get_gpus():
        return tf.config.list_physical_devices('GPU')

    @staticmethod
    def remove_gpu():
        tf.config.set_visible_devices([], 'GPU')

    @staticmethod
    def set_seed(seed: int = random_state):
        os.environ['PYTHONHASHSEED'] = str(seed)
        os.environ['TF_DETERMINISTIC_OPS'] = '1'
        os.environ['TF_CUDNN_DETERMINISTIC'] = '1'
        random.seed(seed)
        tf.random.set_seed(seed)
        np.random.seed(seed)
        set_random_seed(seed)
        tf.keras.utils.set_random_seed(seed)
        tf.config.experimental.enable_op_determinism()

    def check_directories(self):
        check_directory(self.resources_dir)
        check_directory(self.models_dir)
        check_directory(self.dataset_dir)

    @staticmethod
    def set_verbosity_level(verbose_level: int = verbose_level, rocm_logging_level: int = rocm_logging_level):
        os.environ['MIOPEN_ENABLE_LOGGING'] = f'{1 if rocm_logging_level > 0 else 0}'
        os.environ['MIOPEN_ENABLE_LOGGING_CMD'] = f'{1 if rocm_logging_level > 0 else 0}'
        os.environ['MIOPEN_LOG_LEVEL'] = f'{rocm_logging_level if rocm_logging_level > 0 else 0}'
        os.environ['TF_CPP_MAX_VLOG_LEVEL'] = f'{rocm_logging_level}'
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = f'{rocm_logging_level}'
        os.environ['HSAKMT_DEBUG_LEVEL'] = f'{rocm_logging_level}'
        tf.autograph.set_verbosity(verbose_level)

    def set_threads_number(self):
        num_threads = multiprocessing.cpu_count() if self.use_all_threads else self.num_threads
        os.environ["OMP_NUM_THREADS"] = f"{num_threads}"
        os.environ["TF_NUM_INTRAOP_THREADS"] = f"{num_threads}"
        os.environ["TF_NUM_INTEROP_THREADS"] = f"{num_threads}"
        tf.config.threading.set_inter_op_parallelism_threads(num_threads)
        tf.config.threading.set_intra_op_parallelism_threads(num_threads)

    def print_envs(self):
        envs = [
            f'MIOPEN_ENABLE_LOGGING: {os.environ["MIOPEN_ENABLE_LOGGING"]}',
            f'MIOPEN_ENABLE_LOGGING_CMD: {os.environ["MIOPEN_ENABLE_LOGGING_CMD"]}',
            f'MIOPEN_LOG_LEVEL: {os.environ["MIOPEN_LOG_LEVEL"]}',
            f'TF_CPP_MAX_VLOG_LEVEL: {os.environ["TF_CPP_MAX_VLOG_LEVEL"]}',
            f'TF_CPP_MIN_LOG_LEVEL: {os.environ["TF_CPP_MIN_LOG_LEVEL"]}',
            f'HSAKMT_DEBUG_LEVEL: {os.environ["HSAKMT_DEBUG_LEVEL"]}',
            f'OMP_NUM_THREADS: {os.environ["OMP_NUM_THREADS"]}',
            f'TF_NUM_INTRAOP_THREADS: {os.environ["TF_NUM_INTRAOP_THREADS"]}',
            f'TF_NUM_INTEROP_THREADS: {os.environ["TF_NUM_INTEROP_THREADS"]}',
        ]
        self.logger.info('\n' + '\n'.join(envs))

    def set_devices(self):
        if not self.use_gpu:
            self.remove_gpu()
        else:
            if self.limit_gpu_memory:
                gpus = self.get_gpus()
                for gpu in gpus:
                    tf.config.experimental.set_memory_growth(gpu, True)
