# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
import sys

sys.path.append('./src')
sys.path.append('./test')

setup(
    name='takasho-tutrial/python',
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    description="tutrial",
    test_suite='test'
)
