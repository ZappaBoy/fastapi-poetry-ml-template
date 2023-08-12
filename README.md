# Fastapi poetry ML template

## Introduction

This is a template used to build ML models and serving them through `Fastapi` and managing the dependencies using
the `poetry` package manager.
This template offer a solid structure to build complex projects and a lot of pre-built function that allow to focus only
on the model development.
Pre-built functions:

- [x] Pre-installed ML libraries (tensorflow, scikit-learn, matplotlib, pandas)
- [x] CPU/GPU specific libraries versions (CPU only, Nvidia, AMD ROCm)
- [x] API-KEY integration
- [x] Parallelization and Threading utilities methods
- [x] Logging and log-levels support
- [x] Environment management (development, testing, staging, production)
- [x] Pydantic ORM models
- [x] Generic exception handling middleware
- [x] Singleton class
- [x] Environment variables and Fastapi Settings support
- [x] Docker and docker-compose containerization
- [x] Pytest integration with poetry and Fastapi routes testing
- [x] Python 3.11 version
- [x] Dataset and generated resources directory management
- [x] Reproducibility seed global setting
- [x] Fastapi OpenAPI documentation and web api testing environment
- [x] Health check endpoint and docker health integration

## Create `.env`

```shell
ENVIRONMENT=development
PORT=4000
LOG_LEVEL=debug
ALLOWED_HOSTS=["*"]
NUM_THREADS=16
API_KEY_HEADER=x-api-key
API_KEY=your_api_key
# Set to True to enable the predictor initialization and model training
INIT_MODEL=True
# Uncomment to enable ROCm support, change its value according to used GPU
# HSA_OVERRIDE_GFX_VERSION=10.3.0
```

## Install the requirements

Install the requirements using poetry and defining the extra group based on your system:

```shell
# CPU only support
poetry install --with cpu
# Nvidia support
poetry install --with nvidia
# AMD ROCm support
poetry install --with amd
```

## ROCm support

If you are using a rocm compatible AMD GPU you can run the model using GPU.
You simply need to install the rocm binaries and setting the following environment variable:

```shell
HSA_OVERRIDE_GFX_VERSION=10.3.0
```

## Checking endpoint

```shell
curl -X GET 'http://localhost:4000/api/v1/model/predict?data=test_data' -H "x-api-key: your_api_key"
```

## Known issues

Actually `tensorflow-rocm` is not installed using poetry due to an open issue that I tried to fix but is not yet been
merged.
You can simply temporarily install it using pip (pip install tensorflow-rocm) until the issue will be fixed.

## Acknowledgement

This template was created using a lot of open-source project, tools and contributions. Please support all the used
technologies and help their community to expand and improve their quality.
The open-source concept allow people like me to build template like this, and this sort of utils helps other to build
other useful things.
Closed-source projects maybe can do your happiness, but open-source can improve the life of the whole world.