# pylint: disable=C0114
import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

with open(here / "README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="prefix_tree",
    version="0.0.9",
    author="ice1x",
    author_email="ice2600x@gmale.com",
    description="A pure Python prefix tree (trie) for fast in-memory prefix search and filtering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ice1x/prefix_tree",
    project_urls={
        "Documentation": "https://github.com/ice1x/prefix_tree",
        "Source": "https://github.com/ice1x/prefix_tree",
        "Tracker": "https://github.com/ice1x/prefix_tree/issues",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
