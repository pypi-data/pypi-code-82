from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Random Person Generator API'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
       # the name must match the folder name 'random_person_api'
        name="random_person_api", 
        version=VERSION,
        author="Dipen Shah",
        author_email="dipenmshah8@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'random person generator'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)