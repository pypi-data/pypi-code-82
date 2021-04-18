# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['camel_converter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'camel-converter',
    'version': '0.1.0',
    'description': 'Converts a string from snake case to camel case or camel case to snake case',
    'long_description': '# Camel Converter\n\n[![CI Status](https://github.com/sanders41/camel-converter/workflows/CI/badge.svg?branch=main&event=push)](https://github.com/sanders41/camel-converter/actions?query=workflow%3CI+branch%3Amain+event%3Apush)\n[![Coverage](https://codecov.io/github/sanders41/camel-converter/coverage.svg?branch=main)](https://codecov.io/gh/sanders41/camel-converter)\n[![PyPI version](https://badge.fury.io/py/camel-converter.svg)](https://badge.fury.io/py/camel-converter)\n\nIn JSON keys are frequently in camelCase format, while variable names in Python typically\nsnake_case. The purpose of this pacakgae is to help convert between the two formats.\n\n## Usage\n\n- To convert from camel case to snake case:\n\n  ```py\n  from camel_converter import to_snake\n\n  snake = to_snake("myString")\n  ```\n\n  This will convert `myString` into `my_string`\n\n- To convert from snake case to camel case:\n\n  ```py\n  from camel_converter import to_camel\n\n  camel = to_camel("my_string")\n  ```\n\n  This will convert `my_string` into `myString`\n\n- To convert from snake to upper camel case:\n\n  ```py\n  from camel_converter import to_upper_camel\n\n  upper_camel = to_upper_camel("my_string")\n  ```\n\n  This will convert `my_string` into `MyString`\n\nIf you are using [Pydantic](https://pydantic-docs.helpmanual.io/), a common usage of Pydantic where\nthis package is useful is in [FastAPI](https://fastapi.tiangolo.com/) you can use this package in\nyour models to automatically do the conversion.\n\n```py\nfrom pydantic import BaseModel\n\nfrom camel_converter import to_camel\n\n\nclass MyModel(BaseModel):\n    class Config:\n        alias_generator = to_camel\n        allow_population_by_field_name = True\n\n    my_field: str\n```\n\nWith setting up your model in this way `myField` from the source, i.e. JSON data, will map to `my_field` in your model.\n\nYou can also setup a model to inherit the config settings from so the `class Config` does not have to be manually set on every model:\n\n```py\nfrom pydantic import BaseModel\n\nfrom camel_converter import to_camel\n\n\nclass MyBaseModel(BaseModel):\n    class Config:\n        alias_generator = to_camel\n        allow_population_by_field_name = True\n\n\nclass MyModel(MyBaseModel):\n    my_field: str\n\n\nclass AnotherModel(MyBaseModel):\n    another_field: int\n```\n\n## Contributing\n\nIf you are interesting in contributing to this project please see our [contributing guide](CONTRIBUTING.md)\n',
    'author': 'Paul Sanders',
    'author_email': 'psanders1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
