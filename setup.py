from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="prefix_tree",
    version="0.0.6",
    author="ice1x",
    author_email="ice2600x@gmale.com",
    description="A Python Prefix Tree - in memory data base with access by prefix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ice1x.github.io/prefix_tree/",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
