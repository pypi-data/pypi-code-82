# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot', 'nonebot.adapters.cqhttp']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.17.0,<0.18.0', 'nonebot2>=2.0.0-alpha.13,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-adapter-cqhttp',
    'version': '2.0.0a13',
    'description': 'OneBot(CQHTTP) adapter for nonebot2',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://raw.githubusercontent.com/nonebot/nonebot2/master/docs/.vuepress/public/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# NoneBot-Adapter-CQHTTP\n\n_✨ OneBot(CQHTTP) 协议适配 ✨_\n\n</div>\n',
    'author': 'yanyongyu',
    'author_email': 'yyy@nonebot.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://v2.nonebot.dev/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
