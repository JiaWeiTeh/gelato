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
    
    'Article':{
        'cn': '冠詞',
        },
    
    'Article (Challenge)':{
        'cn': '冠詞（挑战）',
        },
    
    'Settings':{
        'cn': '设置',
        },
    
    'Exit':{
        'cn': '推出',
        },
    
    '\nEntering %s mode....\n':{
        'cn': '\n进入%s模式....\n',
        },
    
    'Quiz mode not recognised. The program will now terminate.':{
        'cn': '无法识别测验模式。程序将终止。',
        },
    
    'The program will now terminate.':{
        'cn': '程序将终止。',
        },    
    
    'Here are the correct answers for the part(s) where you made mistakes:':{
        'cn': '这里是您答错部分的正确答案：',
        },

    'What are the correct articles for these nouns?':{
        'cn': '这些名词的正确冠词是什么？',
        },

    'Would you like to review the database before the quiz starts?':{
        'cn': '在测验开始之前，您想要复习数据库吗？',
        },
    
    '(Incorrect)':{
        'cn': '(回答错误)',
        },
    
    'You have successfully answered %s questions correctly!':{
        'cn': '您成功回答了%s个问题！',
        },
    
    'Congratulations! You have successfully completed the entire exercise. Would you like to redo the exercises?':{
        'cn': '恭喜，您已成功完成整个练习！您想再来一次吗？',
        },
    
    '\nExiting GELATO...':{
        'cn': '正在退出 GELATO...',
        },
    
    "Congratulations on achieving a high score! Please enter your username: ":{
        'cn': '恭喜您获得了前三名！请输入您的用户名：',
        },
    "Your username exceeds the maximum length of 10 characters. Please try again.":{
        'cn': '您的用户名超过了最大长度限制(10个字符)。请重新输入。',
        },
    
    "Here are the top three high scores:":{
        'cn': '这是前三名的分数：',
        },
    
    "Date":{
        'cn': '日期',
        },
    
    "Score":{
        'cn': '分数',
        },
    
    "User":{
        'cn': '用户',
        },
    
    
    
    
    }

from random import randrange

prompt = {}

if selected_language == 'en':
    for key, val in prompt_raw.items():
        prompt[key] = key
if selected_language == 'katze':
    for key, val in prompt_raw.items():
        meow_length = 'Meo'+'o'*randrange(5)+'w ' 
        prompt[key] = meow_length*(randrange(2)+1) + ['?', '.', '!','.','??'][randrange(5)]
else:
    for key, val in prompt_raw.items():
        prompt[key] = val[selected_language]




