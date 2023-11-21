#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:37:22 2023

@author: Jia Wei Teh
"""
import time
import sys
from artikel import artikel
from verben import verben
import settings.settings as settings
from language.dictionary import prompt

def display(config, style = '1'):
    
    exec('cone%s()'%style)   
    if config.general.name != None:
        print('\t\t'+prompt['Hello']+' %s!'%config.general.name[:10])
    print('\t\t'+prompt['Welcome to']+' \033[32m'+link('https://github.com/JiaWeiTeh/gelato', 'GELATO')+'\033[39m (GErman Learning Assist TOol)')
    print('\t\t'+prompt['[Version 1.2] July 2023. All rights reserved.'])
    print('\t\t--------------------------------------------------')
    print('\t\t'+prompt['Here are the available learning modes for GELATO:']+'\n')

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


def link(url, label = None):
    if label is None: 
        label = url
    parameters = ''
    # OSC 8 ; params ; URL ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, url, label)


def mode_selection(config):
    
    modes_dict = {'1': prompt['Article'],
                  '2': prompt['Article (Challenge)'],
                  '3': 'Verben',
                  '4': prompt['Settings'],
                  '0': prompt['Exit']
                  }
    for key, value in modes_dict.items():
        print('\t\t'+str(key)+':', value)
        
    print('\t\t'+prompt['If you wish to quit at any time, press CRTL+C'])
    print('\t\t--------------------------------------------------')

    # user select mode
    input_mode = input('\n'+prompt['Please enter the quiz mode (number): ']).replace(" ", "")
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
            print(prompt['\nEntering %s mode....\n']%true_mode)
            time.sleep(.75)
            artikel.run(config, survival=False)
        elif input_mode == '2':
            print(prompt['\nEntering %s mode....\n']%true_mode)
            time.sleep(.75)
            artikel.run(config, survival=True)        
        elif input_mode == '3':
            verben.run(config, survival=True)
        elif input_mode == '4':
            settings.edit_param()
        elif input_mode == '0':
            sys.exit(prompt['The program will now terminate.'])
    else:
        print(prompt['Quiz mode not recognised. The program will now terminate.'])
    return
