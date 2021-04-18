# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nornir_cli',
 'nornir_cli.common_commands',
 'nornir_cli.custom_commands',
 'nornir_cli.plugin_commands',
 'nornir_cli.transform']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'genie==20.9',
 'netmiko==3.3.3',
 'nornir-jinja2==0.1.2',
 'nornir-napalm==0.1.2',
 'nornir-netbox>=0.2.0,<0.3.0',
 'nornir-netmiko==0.1.1',
 'nornir-scrapli==2021.01.30',
 'nornir-utils==0.1.2',
 'nornir==3.1.0',
 'scrapli-community==2021.01.30',
 'scrapli-netconf==2021.01.30',
 'scrapli==2021.01.30',
 'ttp>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['nornir_cli = nornir_cli.nornir_cli:init_nornir_cli']}

setup_kwargs = {
    'name': 'nornir-cli',
    'version': '0.2.0',
    'description': 'Nornir CLI',
    'long_description': '[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![PyPI](https://img.shields.io/pypi/v/nornir-cli.svg)](https://pypi.org/project/nornir-cli)\n[![License: MIT](https://img.shields.io/badge/License-MIT-blueviolet.svg)](https://opensource.org/licenses/MIT)\n[![Docs](https://img.shields.io/badge/docs-passing-green.svg)](https://timeforplanb123.github.io/nornir_cli/)\n\nnornir_cli\n==========\n\n---\n\n**Documentation**: <a href="https://timeforplanb123.github.io/nornir_cli" target="_blank">https://timeforplanb123.github.io/nornir_cli</a>\n\n---\n\n**nornir_cli** is CLI tool based on <a href="https://github.com/nornir-automation/nornir" target="_blank">Nornir framework</a>,\n<a href="https://nornir.tech/nornir/plugins/" target="_blank">Nornir Plugins</a> and <a href="https://github.com/pallets/click" target="_blank">Click</a>\n\n\n## Features \n\n* **Manage your custom nornir runbooks**\n\n    * Create and manage your own runbooks collections\n    * Add your custom nornir runbooks to runbooks collections and run it for any hosts directly from the CLI \n    * Or use `nornir_cli` for inventory management only, and take the result in your nornir runbooks. By excluding getting and filtering the inventory in your runbooks, you will make them more versatile.\n\n* **Manage Inventory**\n\n    Get Inventory, filter Inventory, output Inventory and save Inventory state from the CLI.\n    This is really useful for large, structured Inventory - for example, <a href="https://github.com/netbox-community/netbox" target="_blank">NetBox</a> with <a href="https://github.com/wvandeun/nornir_netbox" target="_blank">nornir_netbox plugin</a>.\n\n* **Run Nornir Plugins**\n\n    Run Tasks based on Nornir Plugins from the CLI, check result and statistic\n\n* **Build a chain of `nornir_cli` commands**\n\n    Initialize Nornir, filter Inventory and start Task/Tasks chains or runbook/runbooks chains in one command\n\n* **Json input. Json output**\n\n    Json strings are everywhere! Ok, only in commands options\n\n* **Custom Multi Commands with click**\n\n    `nornir_cli` based on click Custom Multi Commands, so you can easily add your custom command by following some principles\n\n* **Simple CLI network orchestrator**\n\n    `nornir_cli` is a simple CLI orchestrator that you can use to interact with the SoT and manage your network\n\n## Quick Start \n\n#### Install\n\nPlease, at first, check the dependencies in `pyproject.toml` and create new virtual environment if necessary and then:\n\n**with pip:**\n\n```text\npip install nornir_cli\n```\n\n**with git:**\n\n```text\ngit clone https://github.com/timeforplanb123/nornir_cli.git\ncd nornir_cli\npip install .\n# or\npoetry install\n```\n\n**with Docker:**\n\n```text\ngit clone https://github.com/timeforplanb123/nornir_cli.git\ncd nornir_cli\ndocker build -t timeforplanb123/nornir_cli .\ndocker run --rm -it timeforplanb123/nornir_cli sh\n\n# nornir_cli --version\nnornir_cli, version 0.2.0\n\n```\n\n#### Simple Example\n\n\n#### config.yaml\n```yaml\n# Simple Nornir configuration file\ninventory:\n    plugin: SimpleInventory\n    options:\n        host_file: "inventory/hosts.yaml"\n```\n#### hosts.yaml\n```yaml\n# Single host inventory\ndev_1:\n    hostname: 10.1.0.1\n    username: username \n    password: password\n    # huawei is just an example here\n    platform: huawei\n```\n#### nornir_cli\n```text\n# As instance, let\'s run netmiko_send_command\n\n$ nornir_cli nornir-netmiko init netmiko_send_command --command_string "display clock"\n\nnetmiko_send_command************************************************************\n* dev_1 ** changed : False *****************************************************\nvvvv netmiko_send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO\n2021-03-17 14:04:22+03:00\nWednesday\nTime Zone(Moscow) : UTC+03:00\n^^^^ END netmiko_send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\ndev_1                                             : ok=1               changed=0               failed=0\n\nOK      : 1\nCHANGED : 0\nFAILED  : 0\n```\n',
    'author': 'Pavel Shemetov',
    'author_email': 'timeforplanb123@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/timeforplanb123/nornir_cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
