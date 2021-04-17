# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bgmi',
 'bgmi.downloader',
 'bgmi.front',
 'bgmi.lib',
 'bgmi.utils',
 'bgmi.website']

package_data = \
{'': ['*'], 'bgmi': ['others/*'], 'bgmi.front': ['templates/*']}

install_requires = \
['beautifulsoup4==4.9.3',
 'icalendar==4.0.7',
 'importlib-metadata==3.7.3',
 'peewee==3.14.4',
 'pydantic==1.8.1',
 'requests==2.25.1',
 'tornado==6.1',
 'transmission-rpc==3.2.4',
 'wcwidth>=0.2.5,<0.3.0']

entry_points = \
{'console_scripts': ['bgmi = bgmi.main:main',
                     'bgmi_http = bgmi.front.server:main']}

setup_kwargs = {
    'name': 'bgmi',
    'version': '2.2.0',
    'description': 'BGmi is a cli tool for subscribed bangumi.',
    'long_description': '# BGmi\n\nBGmi is a cli tool for subscribed bangumi.\n\n[中文说明](./README.cn.md)\n\n[![pypi](https://img.shields.io/pypi/v/bgmi.svg)](https://pypi.python.org/pypi/bgmi) [![download](https://pepy.tech/badge/bgmi/month)](https://pepy.tech/project/bgmi) [![pipeline](https://dev.azure.com/BGmi/BGmi/_apis/build/status/BGmi.BGmi?branchName=master)](https://dev.azure.com/BGmi/BGmi/_apis/build/status/BGmi.BGmi?branchName=master) [![coverage](https://codecov.io/gh/BGmi/BGmi/branch/master/graph/badge.svg)](https://codecov.io/gh/BGmi/BGmi) [![license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/BGmi/BGmi/blob/master/LICENSE)\n\n## TODO\n\n## Update Log\n\n- New download delegate [qbittorrent-webapi](https://www.qbittorrent.org/)\n- Remove python 3.5 support as it has reached its end-of-life\n- Remove python 3.4 support as it has reached its end-of-life\n- Remove Python2 support\n- Transmission rpc authentication configuration\n- New download delegate [deluge-rpc](https://www.deluge-torrent.org/)\n- You can filter search results by min and max episode\n\nmore details can be found at [changelog.md](./changelog.md)\n\n## Feature\n\n- Multi data sources supported: [bangumi\\_moe](https://bangumi.moe), [mikan\\_project](https://mikanani.me) or [dmhy](https://share.dmhy.org/)\n- Use aria2, transmission, deluge or qbittorrent to download bangumi\n- Web interface to manage bangumi with HTTP API\n- Play bangumi online with danmaku\n- RSS feed for uTorrent, ICS calendar for mobile devices\n- Bangumi Script: Write your own bangumi parser!\n- Bangumi calendar / episode information\n- Keyword, subtitle group, regular expression filters for download bangumi\n- Windows, Linux and Router system supported, BGmi everywhere\n\n![image](./images/bgmi_cli.png?raw=true%0A%20:alt:%20BGmi%0A%20:align:%20center)\n\n![image](./images/bgmi_http.png?raw=true%0A%20:alt:%20BGmi%20HTTP%20Service%0A%20:align:%20center)\n\n![image](./images/bgmi_player.png?raw=true%0A%20:alt:%20BGmi%20HTTP%20Service%0A%20:align:%20center)\n\n![image](./images/bgmi_admin.png?raw=true%0A%20:alt:%20BGmi%20HTTP%20Service%0A%20:align:%20center)\n\n## Installation\n\nUsing pip:\n\n``` bash\npip install bgmi\n```\n\nOr from source(not recommended):\n\n``` bash\ngit clone https://github.com/BGmi/BGmi\ncd BGmi\npython -m pip install -U pip\npip install .\n```\n\nInit BGmi database and install BGmi web interface:\n\n``` bash\nbgmi install\n```\n\n## Upgrade\n\n``` bash\npip install bgmi -U\nbgmi upgrade\n```\n\nMake sure to run bgmi upgrade after you upgrade your bgmi\n\n## Docker\n\ngo to [BGmi/bgmi-docker-all-in-one](https://github.com/BGmi/bgmi-docker-all-in-one)\n\n## Usage of bgmi\n\nCli completion(bash and zsh. Shell was detected from your env \\$SHELL)\n\n``` bash\neval "$(bgmi complete)"\n```\n\nIf you want to setup a custom BGMI\\_PATH instead of default `$HOME/.bgmi`:\n\n``` bash\nBGMI_PATH=/bgmi bgmi -h\n```\n\nOr add this code to your .bashrc file:\n\n``` bash\nalias bgmi=\'BGMI_PATH=/tmp bgmi\'\n```\n\nSupported data source:\n\n- [bangumi\\_moe(default)](https://bangumi.moe)\n- [mikan\\_project](https://mikanani.me)\n- [dmhy](https://share.dmhy.org/)\n\n### Help\n\nyou can add `--help` to all `BGmi` sub command to show full options, some of them are not mentioned here.\n\n### Change data source\n\n**All bangumi info in database will be deleted when changing data source!** but scripts won\'t be affected\n\nvideo files will still be stored on the disk, but won\'t be shown on website.\n\n``` console\nbgmi source mikan_project\n```\n\n### Show bangumi calendar\n\n``` bash\nbgmi cal\n```\n\n### Subscribe bangumi\n\n``` bash\nbgmi add "Re:CREATORS" "夏目友人帐 陆" "进击的巨人 season 2"\nbgmi add "樱花任务" --episode 0\n```\n\nDefault episode will be the latest episode.\nIf you just add a bangumi that you haven\'t watched any episodes, considering `bgmi add $BANGUMI_NAME --episode 0`.\n\n### Unsubscribe bangumi\n\n``` bash\nbgmi delete --name "Re:CREATORS"\n```\n\n### Update bangumi\n\nUpdate bangumi database (which locates at \\~/.bgmi/bangumi.db acquiescently):\n\n``` bash\nbgmi update --download # download all undownloaded episode fo all followed bangumi\nbgmi update "从零开始的魔法书" --download 2 3 # will download specific episide 2 and 3\nbgmi update "时钟机关之星" --download # will download all undownloaded episode for specific bangumi\n```\n\n### Filter download\n\nSet up the bangumi subtitle group filter and fetch entries:\n\n``` bash\nbgmi list\nbgmi fetch "Re:CREATORS"\nbgmi filter "Re:CREATORS" --subtitle "DHR動研字幕組,豌豆字幕组" --include 720P --exclude BIG5\nbgmi fetch "Re:CREATORS"\n# remove subtitle, include and exclude keyword filter and add regex filter\nbgmi filter "Re:CREATORS" --subtitle "" --include "" --exclude ""\nbgmi filter "Re:CREATORS" --regex "(DHR動研字幕組|豌豆字幕组).*(720P)"\nbgmi fetch "Re:CREATORS"\n```\n\n### Search episodes\n\n``` bash\nbgmi search \'为美好的世界献上祝福！\' --regex-filter \'.*动漫国字幕组.*为美好的世界献上祝福！.*720P.*\'\n# download\nbgmi search \'为美好的世界献上祝福！\' --regex-filter \'.*合集.*\' --download\n```\n\n### Modify downloaded bangumi episode\n\n``` bash\nbgmi list\nbgmi mark "Re:CREATORS" 1\n```\n\nThis will tell bgmi to not need to download episode less than or equal to 1.\n\n### Manage download items\n\n``` bash\nbgmi download --list\nbgmi download --list --status 0\nbgmi download --mark 1 --status 2\n```\n\nStatus code:\n\n- 0 - Not downloaded items\n- 1 - Downloading items\n- 2 - Downloaded items\n\n### Show BGmi configure and modify it\n\n``` bash\nbgmi config\nbgmi config ARIA2_RPC_TOKEN \'token:token233\'\n```\n\nFields of configure file:\n\nBGmi configure:\n\n- `BANGUMI_MOE_URL`: url of bangumi.moe mirror\n- `SAVE_PATH`: bangumi saving path\n- `DOWNLOAD_DELEGATE`: the ways of downloading bangumi (aria2-rpc, transmission-rpc, xunlei, deluge-rpc, qbittorrent-webapi)\n- `MAX_PAGE`: max page for fetching bangumi information\n- `TMP_PATH`: just a temporary path\n- `DANMAKU_API_URL`: url of danmaku api\n- `LANG`: language\n\nAria2-rpc configure:\n\n- `ARIA2_RPC_URL`: aria2c daemon RPC url, not jsonrpc url.("<http://localhost:6800/rpc>" for localhost)\n- `ARIA2_RPC_TOKEN`: aria2c daemon RPC token("token:" for no token)\n\nXunlei configure:\n\nXunlei-Lixian is deprecated, please choose aria2-rpc or transmission-rpc.\n\n- `XUNLEI_LX_PATH`: path of xunlei-lixian binary\n\nTransmission-rpc configure:\n\n- `TRANSMISSION_RPC_URL`: transmission rpc host\n- `TRANSMISSION_RPC_PORT`: transmission rpc port\n- `TRANSMISSION_RPC_USERNAME`: transmission rpc username (leave it default if you don\'t set rpc authentication)\n- `TRANSMISSION_RPC_PASSWORD`: transmission rpc password (leave it default if you don\'t set rpc authentication)\n\nDeluge-rpc configure:\n\n- `DELUGE_RPC_URL`: deluge rpc url\n- `DELUGE_RPC_PASSWORD`: deluge rpc password\n\nqbittorrent-webapi configure:\n\n- `QBITTORRENT_HOST`: qbittorrent WebAPI host\n- `QBITTORRENT_PORT`: qbittorrent WebAPI port\n- `QBITTORRENT_USERNAME`: qbittorrent WebUI username\n- `QBITTORRENT_PASSWORD`: qbittorrent WebUI password\n- `QBITTORRENT_CATEGORY`: qbittorrent new task category (leave it default if you don\'t need to set category)\n\n### Usage of bgmi\\_http\n\nDownload all bangumi cover first:\n\n``` bash\nbgmi cal --download-cover\n```\n\nDownload frontend static files(you may have done it before):\n\n``` bash\nbgmi install\n```\n\nStart BGmi HTTP Service bind on 0.0.0.0:8888:\n\n``` bash\nbgmi_http --port=8888 --address=0.0.0.0\n```\n\n### Use bgmi\\_http on Windows\n\nJust start your bgmi\\_http and open [<http://localhost:8888/>](http://localhost:8888/) in your browser.\n\nConsider most people won\'t use Nginx on Windows, bgmi\\_http use tornado.web.StaticFileHandler to serve static files(frontend, bangumi covers, bangumi files) without Nginx.\n\n### Use bgmi\\_http on Linux\n\nGenerate Nginx config\n\n``` bash\nbgmi gen nginx.conf --server-name bgmi.whatever.com > bgmi.whatever.com\n```\n\nOr write your config file manually.\n\n``` nginx\nserver {\n    listen 80;\n    server_name bgmi;\n\n    root /path/to/bgmi;\n    autoindex on;\n    charset utf-8;\n\n    location /bangumi {\n        # ~/.bgmi/bangumi\n        alias /path/to/bangumi;\n    }\n\n    location /api {\n        proxy_pass http://127.0.0.1:8888;\n        # Requests to api/update may take more than 60s\n        proxy_connect_timeout 500s;\n        proxy_read_timeout 500s;\n        proxy_send_timeout 500s;\n    }\n\n    location /resource {\n        proxy_pass http://127.0.0.1:8888;\n    }\n\n    location / {\n        # ~/.bgmi/front_static/;\n        alias /path/to/front_static/;\n    }\n\n}\n```\n\nOf cause you can use [yaaw](https://github.com/binux/yaaw/) to manage download items if you use aria2c to download bangumi.\n\n``` nginx\n...\nlocation /yaaw {\n    alias /path/to/yaaw;\n}\n\nlocation /jsonrpc {\n    # aria2c rpc\n    proxy_pass http://127.0.0.1:6800;\n}\n...\n```\n\nExample file: [bgmi.conf](https://github.com/BGmi/BGmi/blob/dev/bgmi.conf)\n\n#### DPlayer and Danmaku\n\nBGmi use [DPlayer](https://github.com/DIYgod/DPlayer) to play bangumi.\n\nFirst, setup nginx to access bangumi files. Second, choose one danmaku backend at [DPlayer\\#related-projects](https://github.com/DIYgod/DPlayer#related-projects).\n\nUse bgmi config to setup the url of danmaku api.\n\n``` bash\nbgmi config DANMAKU_API_URL https://api.prprpr.me/dplayer/ # This api is provided by dplayer official\n```\n\n...restart your bgmi\\_http and enjoy :D\n\n#### macOS launchctl service controller\n\nsee [issue \\#77](https://github.com/BGmi/BGmi/pull/77)\n\n[me.ricterz.bgmi.plist](https://github.com/BGmi/BGmi/blob/master/bgmi/others/me.ricterz.bgmi.plist)\n\n## Bangumi Script\n\nBangumi Script is a script which you can write the bangumi parser own. BGmi will load the script and call the method you write before the native functionality.\n\nBangumi Script Runner will catch the data you returned, update the database, and download the bangumi. You only just write the parser and return the data.\n\nBangumi Script is located at BGMI\\_PATH/script, inherited ScriptBase class.\n\nexamples: [script\\_example.py](./script_example.py)\n\n`get_download_url` returns a dict as follows.\n\n``` python\n{\n    1: \'http://example.com/Bangumi/1/1.torrent\',\n    2: \'http://example.com/Bangumi/1/2.torrent\',\n    3: \'http://example.com/Bangumi/1/3.torrent\'\n}\n```\n\nThe keys 1, 2, 3 is the episode, the value is the url of bangumi, make sure your download delegate support it..\n\n## BGmi Data Source\n\nYou can easily add your own BGmi data source by extending BGmi website base class and implement all the method.\n\n``` python\nfrom typing import List, Optional\n\nfrom bgmi.website.base import BaseWebsite\nfrom bgmi.website.model import WebsiteBangumi, Episode\n\n\nclass DataSource(BaseWebsite):\n    def search_by_keyword(\n        self, keyword: str, count: int\n    ) -> List[Episode]:  # pragma: no cover\n        """\n\n        :param keyword: search key word\n        :param count: how many page to fetch from website\n        :return: list of episode search result\n        """\n        raise NotImplementedError\n\n    def fetch_bangumi_calendar(self,) -> List[WebsiteBangumi]:  # pragma: no cover\n        """\n        return a list of all bangumi and a list of all subtitle group\n\n        list of bangumi dict:\n        update time should be one of [\'Sun\', \'Mon\', \'Tue\', \'Wed\', \'Thu\', \'Fri\', \'Sat\', \'Unknown\']\n        """\n        raise NotImplementedError\n\n    def fetch_episode_of_bangumi(\n        self, bangumi_id: str, max_page: int, subtitle_list: Optional[List[str]] = None\n    ) -> List[Episode]:  # pragma: no cover\n        """\n        get all episode by bangumi id\n\n        :param bangumi_id: bangumi_id\n        :param subtitle_list: list of subtitle group\n        :type subtitle_list: list\n        :param max_page: how many page you want to crawl if there is no subtitle list\n        :type max_page: int\n        :return: list of bangumi\n        """\n        raise NotImplementedError\n\n\n    def fetch_single_bangumi(self, bangumi_id: str) -> WebsiteBangumi:\n        """\n        fetch bangumi info when updating\n\n        :param bangumi_id: bangumi_id, or bangumi[\'keyword\']\n        :type bangumi_id: str\n        :rtype: WebsiteBangumi\n        """\n        # return WebsiteBangumi(keyword=bangumi_id) if website don\'t has a page contains episodes and info\n```\n\n## Debug\n\nSet env BGMI\\_LOG to debug, info, warning, error for different log level\n\nlog file will locate at {TMP\\_PATH}/bgmi.log\n\n## Uninstall\n\nScheduled task will not be delete automatically, you will have to remove them manually.\n\n`*nix`:\n\nremove them from your crontab\n\n`windows`:\n\n``` powershell\nschtasks /Delete /TN \'bgmi updater\'\n```\n\n## License\n\n[MIT License](https://github.com/BGmi/BGmi/blob/master/LICENSE)\n',
    'author': 'RicterZ',
    'author_email': 'ricterzheng@gmail.com',
    'maintainer': 'Trim21',
    'maintainer_email': 'i@trim21.me',
    'url': 'https://github.com/BGmi/BGmi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
