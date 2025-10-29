﻿from setuptools import setup, find_packages

setup(
    name="webscraper_futbol",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "beautifulsoup4",
        "html5lib",
    ],
    python_requires=">=3.8",
)
