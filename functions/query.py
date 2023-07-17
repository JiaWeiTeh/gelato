#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 08:50:36 2023

@author: Jia Wei Teh

This script contains functions that set up queries.
"""

def yes_no(question, default = "yes"):
    
    # valid answers
    good_answers = {"yes": True,
                    "y": True,
                    "ja": True,
                    "hao": True,
                    "no": False,
                    "n": False,
                    "nein": False,
                    "buyao": False
                    }
    # set cases for different prompt 
    if default == None:
        prompt = ' (y/n): '
    elif default == "yes":
        prompt = ' (Y/n): '
    elif default == "no":
        prompt = ' (y/N): '
    else:
        raise Exception('invalid default answer for \'%s\''%question)
    # query message
    query = question + prompt
    # loop until a satisfactory answer is given.
    while True:
        answer = input(query).replace(" ", "").lower()
        if default is not None and answer == "":
            return good_answers[default]
        elif answer in good_answers:
            return good_answers[answer]
        else:
            print("Please respond with 'yes' or 'no' " "(or 'y' or 'n').")
    return




