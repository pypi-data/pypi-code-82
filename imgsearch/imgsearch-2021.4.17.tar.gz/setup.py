import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imgsearch",      # Replace with your own username
    version="2021.4.17",
    author="Gamingdy",
    description="A simple image search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gamingdy/image-search-python",
    project_urls={
        "Bug Tracker": "https://github.com/gamingdy/image-search-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)