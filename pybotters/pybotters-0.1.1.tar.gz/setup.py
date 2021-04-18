# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybotters', 'pybotters.models']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'pybotters',
    'version': '0.1.1',
    'description': 'An advanced api client for python botters.',
    'long_description': "# [BETA] pybotters\n\nAn advanced api client for python botters.\n\n## 📌 Description\n\n`pybotters`は[仮想通貨botter](https://note.com/hht/n/n61e6ecefd059)向けのPythonライブラリです。\n\n複数取引所に対応した非同期I/OのAPIクライアントであり、bot開発により素晴らしいDXを提供します。\n\n## 👩\u200d💻👨\u200d💻 In development\n\n`pybotters` は現在 ** **BETAバージョン** ** です。\n一部機能は開発中です。\n\n正式バージョンの開発状況については [こちら](https://github.com/MtkN1/pybotters/issues/25) を参照してください。\n\n## 🚀 Features\n\n- ✨ HTTP / WebSocket Client\n    - 複数取引所のプライベートAPIを自動認証\n    - [`aiohttp`](https://docs.aiohttp.org/)ライブラリを基盤とした非同期通信\n    - WebSocketの自動再接続、自動ハートビート\n- ✨ DataStore\n    - WebSocket用の自動データ保管クラス\n    - 参照渡しによる高速なデータ参照\n    - 取引所別データモデルの実装\n- ✨ Developer Experience\n    - `asyncio`ライブラリを利用した非同期プログラミング\n    - `typing`モジュールによる型ヒントのサポート\n\n## 🏦 Exchanges\n\n| Name | API auth | DataStore | \n| --- | --- | --- |\n| Bybit | ✅ | ✅ |\n| Binance | ✅ | WIP |\n| FTX | ✅ | WIP |\n| BTCMEX | ✅ | ✅ |\n| BitMEX | ✅ | WIP |\n| bitFlyer | ✅ | WIP |\n| GMO Coin | ✅ | WIP |\n| Liquid | ✅ | WIP |\n| bitbank | ✅ | WIP |\n\n## 🐍 Requires\n\nPython 3.7+\n\n## 🛠 Installation\n\n```sh\npip install pybotters\n```\n\n## 🔰 Usage\n\n### Single exchange\n\n```python\nimport asyncio\nimport pybotters\n\napis = {\n    'bybit': ['BYBIT_API_KEY', 'BYBIT_API_SECRET'],\n}\n\nasync def main():\n    async with pybotters.Client(apis=apis, base_url='https://api.bybit.com') as client:\n        # REST API\n        resp = await client.get('/v2/private/position/list', params={'symbol': 'BTCUSD'})\n        data = await resp.json()\n        print(data)\n\n        # WebSocket API (with print handler)\n        ws = await client.ws_connect(\n            url='wss://stream.bybit.com/realtime',\n            send_json={'op': 'subscribe', 'args': ['trade.BTCUSD', 'order', 'position']},\n            hdlr_json=lambda msg, ws: print(msg),\n        )\n        await ws # this await is wait forever (for usage)\n\ntry:\n    asyncio.run(main())\nexcept KeyboardInterrupt:\n    pass\n```\n\n### Multiple exchanges\n\n```python\napis = {\n    'bybit': ['BYBIT_API_KEY', 'BYBIT_API_SECRET'],\n    'btcmex': ['BTCMEX_API_KEY', 'BTCMEX_API_SECRET'],\n    'binance': ['BINANCE_API_KEY', 'BINANCE_API_SECRET'],\n}\n\nasync def main():\n    async with pybotters.Client(apis=apis) as client:\n        await client.post('https://api.bybit.com/v2/private/order/create', data={'symbol': 'BTCUSD', ...: ...})\n        ...\n        await client.post('https://www.btcmex.com/api/v1/order', data={'symbol': 'XBTUSD', ...: ...})\n        ...\n        await client.post('https://dapi.binance.com/dapi/v1/order', data={'symbol': 'BTCUSD_PERP', ...: ...})\n        ...\n```\n\n## 📖 Wiki\n\n詳しい利用方法は👉[Wikiページへ](https://github.com/MtkN1/pybotters/wiki)\n\n## 🗽 License\n\nMIT\n\n## 💖 Author\n\nhttps://twitter.com/MtkN1XBt\n",
    'author': 'MtkN1',
    'author_email': '51289448+MtkN1@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MtkN1/pybotters',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
