#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 00:08:18 2023

@author: Jia Wei Teh
"""


class cprint:
    # A class that deals with printing with colours in terminal. 
    # e.g., print(f'{cprint.BOLD}This text is bolded{cprint.END}  but this isnt.')
    
    # bolded text to signal that a file is being saved
    symbol = '\u27B3 '
    
    
    BOLD = '\033[1m'
    
    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'
    
    # Link
    LINK = '\033[32m'
    
    # Warning message, but code runs still. 
    WARN = '\033[1m\033[94m'
    
    # Italic
    ITALIC = '\33[3m'
    
    # Blink
    BLINK = '\033[5m'
    
    # FAIL
    FAIL = '\033[1m\033[91m'
    
    # END and clear all colours. This should be included in the end of every operations.
    END = '\033[0m'
