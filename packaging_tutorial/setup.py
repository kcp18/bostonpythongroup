# setup.py is the build script for setuptools. It tells setuptools about 
# your package such as the name and version as well as which code 
# files to include

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="boston_python_group",
    version="0.0.1",
    author="Chanwoo Park",
    author_email="parkchan@brandeis.edu",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    install_requires=['pandas', 'docutils>=0.3'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
