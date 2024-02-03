from setuptools import setup, find_packages #to import the steup and find_package
from typing import List #

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.4"
REPO_NAME = "mongodb_package_raj"
PKG_NAME= "database_connect"
AUTHOR_USER_NAME = "rajaryan13092002"
AUTHOR_EMAIL = "rajaryan13092002@gmail.com"

setup(
    name=PKG_NAME, #name of the package define
    version=__version__, #version define
    author=AUTHOR_USER_NAME, #define author name
    author_email=AUTHOR_EMAIL, #define email
    description="A python package for connecting with database.", #description
    long_description=long_description,#read the readme.md file
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",#github url
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),#src folder
    )
