# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
    ['app',
     'app.routes',
     'app.routes.predict',
     'app.routes.predict.dto',
     'app.services',
     'app.services.model',
     'app.shared',
     'app.shared.decorators',
     'app.shared.deps',
     'app.shared.middlewares',
     'app.shared.models',
     'app.shared.models.settings',
     'app.shared.utilities']

package_data = \
    {'': ['*']}

install_requires = \
    ['fastapi-utils>=0.2.1,<0.3.0',
     'fastapi>=0.95.1,<0.96.0',
     'loguru>=0.7.0,<0.8.0',
     'matplotlib>=3.7.1,<4.0.0',
     'pandas>=2.0.2,<3.0.0',
     'pydantic>=1.10.7,<2.0.0',
     'requests>=2.31.0,<3.0.0',
     'scikit-learn>=1.2.2,<2.0.0',
     'starlette>=0.26.1,<0.27.0',
     'uvicorn>=0.21.1,<0.22.0']

entry_points = \
    {'console_scripts': ['app = app:main', 'test = pytest:main']}

setup_kwargs = {
    'name': 'app',
    'version': '0.1.0',
    'description': 'Fastapi poetry ML template',
    'long_description': '# Fastapi poetry ML template\n\n## Introduction\nThis is a template used to build ML models and serving them through `Fastapi` and managing the dependencies using the `poetry` package manager. \nThis template offer a solid structure to build complex projects and a lot of pre-built function that allow to focus only on the model development.\nPre-built functions:\n- [x] Pre-installed ML libraries (tensorflow, scikit-learn, matplotlib, pandas)\n- [x] CPU/GPU specific libraries versions (CPU only, Nvidia, AMD ROCm) \n- [x] API-KEY integration\n- [x] Parallelization and Threading utilities methods\n- [x] Logging and log-levels support\n- [x] Environment management (development, testing, staging, production)\n- [x] Pydantic ORM models\n- [x] Generic exception handling middleware\n- [x] Singleton class\n- [x] Environment variables and Fastapi Settings support \n- [x] Docker and docker-compose containerization \n- [x] Pytest integration with poetry and Fastapi routes testing\n- [x] Python 3.11 version\n- [x] Dataset and generated resources directory management\n- [x] Reproducibility seed global setting\n- [x] Fastapi OpenAPI documentation and web api testing environment\n- [x] Health check endpoint and docker health integration\n\n\n## Create `.env`\n```shell\nENVIRONMENT=development\nPORT=4000\nLOG_LEVEL=debug\nALLOWED_HOSTS=["*"]\nNUM_THREADS=16\nAPI_KEY_HEADER=x-api-key\nAPI_KEY=your_api_key\n# Set to True to enable the predictor initialization and model training\nINIT_MODEL=True\n# Uncomment to enable ROCm support, change its value according to used GPU\n# HSA_OVERRIDE_GFX_VERSION=10.3.0\n```\n\n## Install the requirements\nInstall the requirements using poetry and defining the extra group based on your system:\n```shell\n# CPU only support\npoetry install --with cpu\n# Nvidia support\npoetry install --with nvidia\n# AMD ROCm support\npoetry install --with amd\n```\n\n## ROCm support\nIf you are using a rocm compatible AMD GPU you can run the model using GPU.\nYou simply need to install the rocm binaries and setting the following environment variable:\n```shell\nHSA_OVERRIDE_GFX_VERSION=10.3.0\n```\n\n## Checking endpoint\n```shell\ncurl -X GET \'http://localhost:4000/api/v1/model/predict?data=test_data\' -H "x-api-key: your_api_key"\n```\n\n## Acknowledgement\nThis template was created using a lot of open-source project, tools and contributions. Please support all the used technologies and help their community to expand and improve their quality.\nThe open-source concept allow people like me to build template like this, and this sort of utils helps other to build other useful things.\nClosed-source projects maybe can do your happiness, but open-source can improve the life of the whole world.',
    'author': 'ZappaBoy',
    'author_email': 'federico.zappone@justanother.cloud',
    'maintainer': 'ZappaBoy',
    'maintainer_email': 'federico.zappone@justanother.cloud',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<3.12',
}

setup(**setup_kwargs)
