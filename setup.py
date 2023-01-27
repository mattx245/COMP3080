#setup file to allow pip install

import setuptools

with open ("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Sample Pythod Package",
    version="1.0.0",
    author="22207000",
    author_email="sample@sample.jp",
    description="A sample package for python. To be run on AWS EC2 ubuntu server",
    url="https://github.com/mattx245/COMP3080/blob/main/sample_package",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)