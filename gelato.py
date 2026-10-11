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
from colorama import just_fix_windows_console


def run():
    # so that the colours and the line overwriting also work in the Windows terminal
    just_fix_windows_console()
    # get parameters
    config = settings.get_param()
    # display header
    header.display(config)
    # available modes
    try:
        header.mode_selection(config)
    except KeyboardInterrupt:
        # end if ctrl+c command is used.
        print(prompt['\nExiting GELATO...'])
    
    return


# run() is also what the 'gelato' command calls (see pyproject.toml)
if __name__ == '__main__':
    run()
