from setuptools import find_packages
from setuptools import setup

setup(
    name='pendulum_msgs',
    version='0.20.5',
    packages=find_packages(
        include=('pendulum_msgs', 'pendulum_msgs.*')),
)
