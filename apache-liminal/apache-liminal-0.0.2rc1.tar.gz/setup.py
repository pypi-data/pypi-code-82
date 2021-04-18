#!/usr/bin/env python3
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import logging
import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    logging.info(requirements)

setuptools.setup(
    name="apache-liminal",
    version=os.environ.get("LIMINAL_BUILD_VERSION", os.environ.get('LIMINAL_VERSION', None)),
    author="dev@liminal.apache.org",
    author_email='dev@liminal.apache.org',
    description="A package for authoring and deploying machine learning workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apache/incubator-liminal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    license='Apache License, Version 2.0',
    python_requires='>=3.6',
    install_requires=requirements,
    scripts=['scripts/liminal'],
    include_package_data=True,
    package_data={
        'liminal': ['../DISCLAIMER', '../LICENSE', '../NOTICE', '../README.md']
    }
)
