import os
from setuptools import find_packages, setup

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()
setup(
    name = "cpalgo",
    version = "0.1.91",
    author = "Narayanaa S R",
    author_email = "srnarayanaa@gmail.com",
    description = ("A python library that contains standard competitive programming algorithms for faster access"),
    license = "BSD",
    keywords = "competitive programming algorithms",
    url = "https://github.com/srnarayanaa/cpalgo/blob/main/README.md", 
    packages = find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown'
)