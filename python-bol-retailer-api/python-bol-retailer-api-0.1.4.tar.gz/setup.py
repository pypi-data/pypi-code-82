from distutils.core import setup

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'python-bol-retailer-api',         
  packages = ['bol'],
  version = '0.1.4',
  license='GPL-3.0-or-later',
  description = 'Wrapper for the bol.com Retailer API (v5)',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Alexander Schillemans',
  author_email = 'alexander.schillemans@lhs.global',
  url = 'https://github.com/alexanderlhsglobal/python-bol-retailer-api',
  download_url = 'https://github.com/alexanderlhsglobal/python-bol-retailer-api/archive/refs/tags/v0.1.4.tar.gz',
  keywords = ['bol.com', 'api'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3.6',
  ],
)