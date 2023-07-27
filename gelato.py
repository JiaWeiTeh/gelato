#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:52:44 2023

@author: Jia Wei Teh

This is the main file.
"""
import functions.header as header
import settings.settings as settings
from language.dictionary import prompt

# get parameters
config = settings.get_param()
# display header
header.display(config)
# available modes
header.mode_selection(config)
# end
print(prompt['\nExiting GELATO...'])