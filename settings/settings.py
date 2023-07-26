#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 16:42:59 2023

@author: Jia Wei Teh
This script retrieves the parameters.
"""


import os
import yaml

def get_param():
    # load
    with open('./settings/settings.yml','r') as file:
        gelato_params = yaml.load(file, Loader=yaml.Loader)
    
    # A simple script that turns dictionaries into objects
    class Dict2Class:
        def __init__(self, data):
            for name, value in data.items():
                setattr(self, name, self._wrap(value))
    
        def _wrap(self, value):
            if isinstance(value, (tuple, list, set, frozenset)): 
                return type(value)([self._wrap(v) for v in value])
            else:
                return Dict2Class(value) if isinstance(value, dict) else value
        
    # return
    return Dict2Class(gelato_params)

def edit_param():
    
    os.system('emacs settings/settings.yml')
    
    return
