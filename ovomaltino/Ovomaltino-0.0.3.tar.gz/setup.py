import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Ovomaltino",
    version="0.0.3",
    author="Matheus Nobre Gomes",
    author_email="matt-gomes@live.com",
    description="Multi agent system using social theories",
    license="GPLv3+",
    keywords="Ovomaltino",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ovomaltino/Ovomaltino",
    packages=['ovomaltino', 'classes', 'database', 'datatype', 'handler', 'utils'],
    install_requires=[
        "numpy",
        "pandas",
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
