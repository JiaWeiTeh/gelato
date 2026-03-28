#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 00:08:18 2023

@author: Jia Wei Teh

Terminal color/style constants for formatted output.
Usage: print(f'{cprint.BOLD}This text is bolded{cprint.END} but this isnt.')
"""


class cprint:
    """ANSI escape code constants for terminal styling."""

    symbol = '\u27B3 '

    BOLD = '\033[1m'

    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'
    WHITE = '\33[37m'

    LINK = '\033[32m'
    WARN = '\033[1m\033[94m'
    ITALIC = '\33[3m'
    BLINK = '\033[5m'
    FAIL = '\033[1m\033[91m'

    # Clear all colours. Should be included at the end of every styled output.
    END = '\033[0m'
