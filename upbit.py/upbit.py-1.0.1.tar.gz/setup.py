from setuptools import setup

setup(
    name='upbit.py',
    version='1.0.1',
    packages=['upbit'],
    url='https://github.com/Beta5051/upbit.py',
    license='MIT',
    author_email='beta5051@gmail.com',
    description='Upbit API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['websockets>=8.1', 'pyjwt>=2.0.1', 'requests>=2.21.0']
)