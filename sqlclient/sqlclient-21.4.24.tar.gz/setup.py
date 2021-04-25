import pathlib
from setuptools import setup, find_packages


HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

name = 'sqlclient'
version = next(open(HERE / f"src/{name.replace('-', '_')}/__init__.py"))
version = version.strip('\n').split('=')[1].strip(" '")

setup(
    name=name,
    version=version,
    description='Python client for SQL',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/zpz/' + name,
    license='MIT',
    python_requires='>=3.6',
    package_dir={'': 'src'},
    packages=[name.replace('-', '_')],
    include_package_data=True,
    install_requires=[
        'pandas',
    ],
)
