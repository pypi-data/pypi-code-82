# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['essencia_pack']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'essencia-pack',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'arantesdv',
    'author_email': 'arantesdv@me.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
