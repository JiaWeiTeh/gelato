#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:15:16 2023

@author: Jia Wei Teh
"""

from setuptools import setup, find_packages

setup(
    name='gelato',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'tabulate',
        'openpyxl',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'gelato=gelato:run'
        ]
    }
)