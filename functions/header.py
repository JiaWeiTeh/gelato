#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:37:22 2023

@author: Jia Wei Teh
"""
import time
import sys
from artikel import artikel

def display(style = '1'):
    
    exec('cone%s()'%style)    
    print('\t\tWelcome to \033[32mGELATO\033[39m (GErman LAnguage Test Online)')
    print('\t\tThis is a (quirky) Python code written by Jia Wei.')
    print('\t\t[Version 0.1] July 2023. All rights reserved.\n\n')
    print('\t\t--------------------------------------------------')
    print('\t\tThese are the available learning modes for GELATO:\n')

    return


def cone1():
    
    print(r"""
       _  
     ,' `,.      ______     ______     __         ______     ______   ______ 
     >-.(__)    /\  ___\   /\  ___\   /\ \       /\  __ \   /\__  _\ /\  __ \   
    (_,-' |     \ \ \__ \  \ \  __\   \ \ \____  \ \  __ \  \/_/\ \/ \ \ \/\ \ 
      `.  |      \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\    \ \_\  \ \_____\ 
        `.|       \/_____/   \/_____/   \/_____/   \/_/\/_/     \/_/   \/_____/ 
          `
        """)

    return 



def cone2():
    
    print(r"""
                  .-"`'"-.
                 /        \
                 |        |      __    ____  _      __   _____  ___  
                 /'---'--`\     / /`_ | |_  | |    / /\   | |  / / \ 
                |          |    \_\_/ |_|__ |_|__ /_/--\  |_|  \_\_/
                \.--.---.-./
                (_.--._.-._)
                  \=-=-=-/
                   \=-=-/
                    \=-/
                     \/
                                     
    """)
    
def mode_selection():
    
    modes_dict = {'1': 'Artikel',
                  '2': 'Artikel (Challenge)',
                  '3': 'Settings',
                  '0': 'Exit'
                  }
    for key, value in modes_dict.items():
        print('\t\t'+str(key)+':', value)
    print('\t\tIf you wish to quit at any time, just press CRTL+C')
    print('\t\t--------------------------------------------------')

    # user select mode
    input_mode = input('\n\nInsert quiz mode (number): ').replace(" ", "")
    # some sleep so that the output is not too quick
    time.sleep(.25)
    # check if modes exist
    if input_mode in list(modes_dict.keys()):
        true_mode = modes_dict[input_mode]
        modeExist = True
    else:
        modeExist = False
    # mode cases
    if modeExist:
        if input_mode == '1':
            print('\nEntering the \"'+true_mode+'\" mode....\n')
            time.sleep(.75)
            artikel.run()
        elif input_mode == '2':
            print('\nEntering the \"'+true_mode+'\" mode....\n')
            time.sleep(.75)
            artikel.run(survival=True)        
        elif input_mode == '3':
            print('Woops! Section TBD.')
        elif input_mode == '0':
            sys.exit('Program ended.')
    else:
        print(f'Mode \"{input_mode}\" not recognised. Ending program!')
    return