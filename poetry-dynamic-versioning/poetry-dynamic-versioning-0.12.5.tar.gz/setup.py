# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_dynamic_versioning']

package_data = \
{'': ['*']}

install_requires = \
['dunamai>=1.5,<2.0', 'jinja2>=2.11.1,<3.0.0', 'tomlkit>=0.4']

entry_points = \
{'console_scripts': ['poetry-dynamic-versioning = '
                     'poetry_dynamic_versioning.__main__:main']}

setup_kwargs = {
    'name': 'poetry-dynamic-versioning',
    'version': '0.12.5',
    'description': 'Plugin for Poetry to enable dynamic versioning based on VCS tags',
    'long_description': '# Dynamic versioning plugin for Poetry\n[![Version](https://img.shields.io/pypi/v/poetry-dynamic-versioning)](https://pypi.org/project/poetry-dynamic-versioning)\n[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n\nThis package is a plugin for [Poetry](https://github.com/sdispater/poetry)\nto enable dynamic versioning based on tags in your version control system,\npowered by [Dunamai](https://github.com/mtkennerly/dunamai). Many different\nversion control systems are supported, including Git and Mercurial; please\nrefer to the Dunamai page for the full list (and minimum supported version\nwhere applicable).\n\nSince Poetry does not yet officially support plugins\n(refer to [this issue](https://github.com/sdispater/poetry/issues/693))\nas of the time of writing on 2019-10-19, this package takes some novel\nliberties to make the functionality possible. As soon as official support\nlands, this plugin will be updated to do things the official way.\n\n## Installation\nPython 3.5+ and Poetry 1.0.2+ or poetry-core 1.0.0+ are required.\n\n* Run `pip install poetry-dynamic-versioning`\n* Add this section to your pyproject.toml:\n  ```toml\n  [tool.poetry-dynamic-versioning]\n  enable = true\n  ```\n* Include the plugin in the `build-system` section of pyproject.toml\n  for interoperability with PEP 517 build frontends.\n  * Example using `poetry-core` as the build system:\n    ```toml\n    [build-system]\n    requires = ["poetry-core>=1.0.0", "poetry-dynamic-versioning"]\n    build-backend = "poetry.core.masonry.api"\n    ```\n  * Example using `poetry` as the build system:\n    ```toml\n    [build-system]\n    requires = ["poetry>=1.0.2", "poetry-dynamic-versioning"]\n    build-backend = "poetry.masonry.api"\n    ```\n\nNote that you must install the plugin in your global Python installation,\n**not** as a dev-dependency in pyproject.toml, because the virtual environment\nthat Poetry creates cannot see Poetry itself and therefore cannot patch it.\n\nPoetry\'s typical `version` setting is still required in `[tool.poetry]`,\nbut you are encouraged to use `version = "0.0.0"` as a standard placeholder.\n\nWith the minimal configuration above, the plugin will automatically take effect\nwhen you run commands such as `poetry build`. It will update the version in\npyproject.toml, then revert the change when the plugin deactivates. If you want\nto include a `__version__` variable in your code, just put a placeholder in the\nappropriate file and configure the plugin to update it (see below) if it isn\'t\none of the defaults. You are encouraged to use `__version__ = "0.0.0"` as a\nstandard placeholder.\n\n## Configuration\nIn your pyproject.toml file, you may configure the following options:\n\n* `[tool.poetry-dynamic-versioning]`: General options.\n  * `enable`: Boolean. Default: false. Since the plugin has to be installed\n    globally, this setting is an opt-in per project. This setting will likely\n    be removed once plugins are officially supported.\n  * `vcs`: String. This is the version control system to check for a version.\n    One of: `any` (default), `git`, `mercurial`, `darcs`, `bazaar`,\n    `subversion`, `fossil`.\n  * `metadata`: Boolean. Default: unset. If true, include the commit hash in\n    the version, and also include a dirty flag if `dirty` is true. If unset,\n    metadata will only be included if you are on a commit without a version tag.\n  * `tagged-metadata`: Boolean. Default: false. If true, include any tagged\n    metadata discovered as the first part of the metadata segment.\n    Has no effect when `metadata` is set to false.\n  * `dirty`: Boolean. Default: false. If true, include a dirty flag in the\n    metadata, indicating whether there are any uncommitted changes.\n    Has no effect when `metadata` is set to false.\n  * `pattern`: String. This is a regular expression which will be used to find\n    a tag representing a version. There must be a capture group named `base`\n    with the main part of the version. Optionally, it may contain another two\n    groups named `stage` and `revision` for prereleases, and it may contain a\n    group named `tagged_metadata` to be used with the `tagged-metadata` option.\n\n    The default is:\n\n    ```re\n    (?x)                                                (?# ignore whitespace)\n    ^v(?P<base>\\d+\\.\\d+\\.\\d+)                           (?# e.g., v1.2.3)\n    (-?((?P<stage>[a-zA-Z]+)\\.?(?P<revision>\\d+)?))?    (?# e.g., beta-0)\n    (\\+(?P<tagged_metadata>.+))?$                       (?# e.g., +linux)\n    ```\n\n    Remember that the backslashes must be escaped (`\\\\`) in the TOML file.\n  * `format`: String. Default: unset. This defines a custom output format for\n    the version. Available substitutions:\n\n    * `{base}`\n    * `{stage}`\n    * `{revision}`\n    * `{distance}`\n    * `{commit}`\n    * `{dirty}`\n    * `{tagged_metadata}`\n\n    Example: `v{base}+{distance}.{commit}`\n  * `format-jinja`: String. Default: unset. This defines a custom output format\n    for the version, using a [Jinja](https://pypi.org/project/Jinja2) template.\n    When this is set, `format` is ignored.\n\n    Available variables:\n\n    * `base` (string)\n    * `stage` (string or None)\n    * `revision` (integer or None)\n    * `distance` (integer)\n    * `commit` (string)\n    * `dirty` (boolean)\n    * `tagged_metadata` (string or None)\n    * `version` (dunumai.Version)\n    * `env` (dictionary of environment variables)\n\n    Available functions:\n\n    * `bump_version` ([from Dunamai](https://github.com/mtkennerly/dunamai/blob/dc2777cdcc5eeff61c10602e33b1a0dc0bb0357b/dunamai/__init__.py#L786-L797))\n    * `serialize_pep440` ([from Dunamai](https://github.com/mtkennerly/dunamai/blob/dc2777cdcc5eeff61c10602e33b1a0dc0bb0357b/dunamai/__init__.py#L687-L710))\n    * `serialize_semver` ([from Dunamai](https://github.com/mtkennerly/dunamai/blob/dc2777cdcc5eeff61c10602e33b1a0dc0bb0357b/dunamai/__init__.py#L740-L752))\n    * `serialize_pvp` ([from Dunamai](https://github.com/mtkennerly/dunamai/blob/dc2777cdcc5eeff61c10602e33b1a0dc0bb0357b/dunamai/__init__.py#L766-L775))\n\n    Simple example:\n\n    ```toml\n    format-jinja = "{% if distance == 0 %}{{ base }}{% else %}{{ base }}+{{ distance }}.{{ commit }}{% endif %}"\n    ```\n\n    Complex example:\n\n    ```toml\n    format-jinja = """\n        {%- if distance == 0 -%}\n            {{ serialize_pep440(base, stage, revision) }}\n        {%- elif revision is not none -%}\n            {{ serialize_pep440(base, stage, revision + 1, dev=distance, metadata=[commit]) }}\n        {%- else -%}\n            {{ serialize_pep440(bump_version(base), stage, revision, dev=distance, metadata=[commit]) }}\n        {%- endif -%}\n    """\n    ```\n  * `format-jinja-imports`: Array of tables. Default: empty. This defines\n    additional things to import and make available to the `format-jinja`\n    template. Each table must contain a `module` key and may also contain an\n    `item` key. Consider this example:\n\n    ```toml\n    format-jinja-imports = [\n        { module = "foo" },\n        { module = "bar", item = "baz" },\n    ]\n    ```\n\n    This is roughly equivalent to:\n\n    ```python\n    import foo\n    from bar import baz\n    ```\n\n    `foo` and `baz` would then become available in the Jinja formatting.\n  * `style`: String. Default: unset. One of: `pep440`, `semver`, `pvp`.\n    These are preconfigured output formats. If you set both a `style` and\n    a `format`, then the format will be validated against the style\'s rules.\n    If `style` is unset, the default output format will follow PEP 440,\n    but a custom `format` will only be validated if `style` is set explicitly.\n  * `latest-tag`: Boolean. Default: false. If true, then only check the latest\n    tag for a version, rather than looking through all the tags until a suitable\n    one is found to match the `pattern`.\n  * `bump`: Boolean. Default: false. If true, then increment the last part of\n    the version `base` by 1, unless the `stage` is set, in which case increment\n    the `revision` by 1 or set it to a default of 2 if there was no `revision`.\n    Does nothing when on a commit with a version tag.\n\n    Example, if there have been 3 commits since the `v1.3.1` tag:\n    * PEP 440 with `bump = false`: `1.3.1.post3.dev0+28c1684`\n    * PEP 440 with `bump = true`: `1.3.2.dev3+28c1684`\n* `[tool.poetry-dynamic-versioning.subversion]`: Options specific to Subversion.\n  * `tag-dir`: String. Default: `tags`. This is the location of tags relative\n    to the root.\n* `[tool.poetry-dynamic-versioning.substitution]`: Insert the dynamic version\n  into additional files other than just pyproject.toml. These changes will be\n  reverted when the plugin deactivates.\n  * `files`: List of globs for any files that need substitutions. Default:\n    `["*.py", "*/__init__.py", "*/__version__.py", "*/_version.py"]`.\n    To disable substitution, set this to an empty list.\n  * `patterns`: List of regular expressions for the text to replace.\n    Each regular expression must have two capture groups, which are any\n    text to preserve before and after the replaced text. Default:\n    `["(^__version__\\s*=\\s*[\'\\"])[^\'\\"]*([\'\\"])"]`.\n\n    Remember that the backslashes must be escaped (`\\\\`) in the TOML file.\n\nSimple example:\n\n```toml\n[tool.poetry-dynamic-versioning]\nenable = true\nvcs = "git"\nstyle = "semver"\n```\n\n## Command line mode\nThe plugin also has a command line mode for execution on demand.\nThis mode applies the dynamic version to all relevant files and leaves\nthe changes in-place, allowing you to inspect the result.\nYour configuration will be detected from pyproject.toml as normal,\nbut the `enable` option is not necessary.\n\nTo activate this mode, run the `poetry-dynamic-versioning` command\nin your console.\n\n## Caveats\n* The dynamic version is not available during `poetry run` because Poetry\n  uses [`os.execvp()`](https://docs.python.org/2/library/os.html#os.execvp).\n* Regarding PEP 517 support:\n\n  `pip wheel .` will not work, because Pip creates an isolated copy of the\n  source code, which does not contain the Git history and therefore cannot\n  determine the dynamic version.\n\n  If you want to build wheels of your dependencies, you **can** do the following,\n  but it won\'t work with path dependencies for the same reason as above:\n\n  ```\n  poetry export -f requirements.txt -o requirements.txt --without-hashes\n  pip wheel -r requirements.txt\n  ```\n\n## Implementation\nIn order to side-load plugin functionality into Poetry, this package\ndoes the following:\n\n* Upon installation, it delivers a `zzz_poetry_dynamic_versioning.pth`\n  file to your Python site-packages directory. This forces Python to\n  automatically load the plugin after all other modules have been loaded\n  (or at least those alphabetically prior to `zzz`).\n* It first tries to patch `poetry.factory.Factory.create_poetry` and\n  `poetry.console.commands.run.RunCommand` directly. If they cannot be\n  imported, then it patches `builtins.__import__` so that, whenever those\n  classes are first imported, then they will be patched. The reason we may have\n  to wait for these to be imported is in case you\'ve used the get-poetry.py\n  script, in which case there is a gap between when Python is fully loaded and\n  when `~/.poetry/bin/poetry` adds the Poetry lib folder to the PYTHONPATH.\n* The patched version of `Factory` will compute and apply the dynamic version.\n* The patched version of `RunCommand` will deactivate the plugin before\n  executing the passed command, because otherwise we will not be able to do\n  any cleanup afterwards.\n\n## Development\nPlease refer to [CONTRIBUTING.md](CONTRIBUTING.md).\n',
    'author': 'Matthew T. Kennerly',
    'author_email': 'mtkennerly@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mtkennerly/poetry-dynamic-versioning',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
