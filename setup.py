import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trie",
    version="0.0.1",
    author="ice1x",
    author_email="ice2600x@gmale.com",
    description="A Python Prefix Tree - in memory data base with access by prefix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/trie",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
