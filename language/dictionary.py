#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:21:52 2023

@author: Jia Wei Teh
"""

from settings import settings


# get parameters
config = settings.get_param()
selected_language = config.general.def_language

prompt_raw = {
    
    'Hello':{ 
            'cn': '哈啰',
            },
    
    'Welcome to':{
        'cn':  '欢迎使用',
        },
    
    '[Version 1.2] July 2023. All rights reserved.':{
        'cn': '[版本 1.2] 2023年7月。版权所有。',
        },
    
    'Here are the available learning modes for GELATO:':{
        'cn': '以下是GELATO可用的学习模式：',
        },
    
    'If you wish to quit at any time, press CRTL+C':{
        'cn': '如果您想随时退出，请按CRTL+C键',
        },
    
    'Please enter the quiz mode (number): ':{
        'cn': '请输入测验模式（数字）： ',
        },
    
    
    }



prompt = {}

for key, val in prompt_raw.items():
    prompt[key] = val[selected_language]


# 无法识别测验模式“{input_mode}”。程序将终止。

# 冠詞

# print('\t\tWelcome to \033[32m'+link('https://github.com/JiaWeiTeh/gelato', 'GELATO')+'\033[39m (GErman LAnguage Test Online)')
