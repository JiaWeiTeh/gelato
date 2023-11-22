#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:15:16 2023

@author: Jia Wei Teh
"""

from setuptools import setup
setup(
    name='gelato',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'gelato=gelato:run'
        ]
    }
)