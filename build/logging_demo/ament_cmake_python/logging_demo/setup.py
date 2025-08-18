from setuptools import find_packages
from setuptools import setup

setup(
    name='logging_demo',
    version='0.20.5',
    packages=find_packages(
        include=('logging_demo', 'logging_demo.*')),
)
