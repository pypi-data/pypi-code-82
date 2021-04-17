# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pythonit_toolkit',
 'pythonit_toolkit.api',
 'pythonit_toolkit.emails',
 'pythonit_toolkit.emails.backends',
 'pythonit_toolkit.headers',
 'pythonit_toolkit.pastaporto',
 'pythonit_toolkit.starlette_backend']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.0.1,<3.0.0', 'boto3>=1.17.39,<2.0.0', 'strawberry-graphql']

setup_kwargs = {
    'name': 'pythonit-toolkit',
    'version': '0.1.38',
    'description': '',
    'long_description': None,
    'author': 'Python Italia',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
