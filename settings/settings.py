#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 16:42:59 2023

@author: Jia Wei Teh
This script retrieves the parameters.
"""


import os
import subprocess
from pathlib import Path
import yaml

# settings.yml sits next to this file
settings_path = Path(__file__).resolve().parent / 'settings.yml'

# used if something is missing in settings.yml
defaults = {'general': {'name': 'User', 'def_language': 'en'},
            'artikel_normal': {'def_qs': None},
            'artikel_challenge': {'hearts': 3},
            }

def get_param():
    # load
    with open(settings_path,'r', encoding = 'utf-8') as file:
        gelato_params = yaml.load(file, Loader=yaml.SafeLoader)
    # in case the file is empty
    if not isinstance(gelato_params, dict):
        gelato_params = {}
    
    # fill in whatever is missing with the defaults
    for section in defaults:
        if not isinstance(gelato_params.get(section), dict):
            gelato_params[section] = {}
        for key in defaults[section]:
            if key not in gelato_params[section]:
                gelato_params[section][key] = defaults[section][key]
    
    # name and language should be text (name: null means no greeting)
    if gelato_params['general']['name'] != None:
        gelato_params['general']['name'] = str(gelato_params['general']['name'])
    gelato_params['general']['def_language'] = str(gelato_params['general']['def_language'])
    # hearts should be a number
    try:
        gelato_params['artikel_challenge']['hearts'] = int(gelato_params['artikel_challenge']['hearts'])
    except (TypeError, ValueError):
        gelato_params['artikel_challenge']['hearts'] = defaults['artikel_challenge']['hearts']
    # def_qs should be a positive number, otherwise None (which means all questions)
    try:
        gelato_params['artikel_normal']['def_qs'] = int(gelato_params['artikel_normal']['def_qs'])
        if gelato_params['artikel_normal']['def_qs'] <= 0:
            gelato_params['artikel_normal']['def_qs'] = None
    except (TypeError, ValueError):
        gelato_params['artikel_normal']['def_qs'] = None
    
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
    
    # open settings.yml with the editor set in $EDITOR, otherwise nano (notepad on Windows)
    editor = os.environ.get('EDITOR', 'notepad' if os.name == 'nt' else 'nano')
    try:
        subprocess.run(editor.split() + [str(settings_path)])
    except FileNotFoundError:
        # imported here, because dictionary.py needs this file to be loaded first
        from language.dictionary import prompt
        print(prompt['Could not open %s. Please edit this file manually: %s']%(editor, settings_path))
    
    return
