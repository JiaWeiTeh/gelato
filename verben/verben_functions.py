#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:17:53 2023

@author: Jia Wei Teh

This script contains functions that are used to run verben.py
"""

from language.dictionary import prompt
from functions.terminal_prints import cprint as cpr
from functions.common import load_excel, randomiser, set_number


# TODO:
    # add prompts
    # add functionality to guess the blank in a sentence.


def load_file():
        
    # Reading an excel file
    data = load_excel("verben.xlsx")
    return data


def qna_section(config, survival):
    
    # read data. The headers are the questions (Präsens, Präteritum, ...)
    data = load_file()
    header_array = list(data.columns)
    data_array = data.to_numpy()
            
    # convert dictionary to list
    # get keys and values
    
    # randomise for QnA, plus set the number of questions
    data_array = randomiser(data_array)
    data_array = data_array[:set_number(len(data_array))]
    
    # begin
    print('       ' + '\u2500'*8 + prompt["# Begin quiz #"] + '\u2500'*8 + '\n')
    # for the score at the end
    correct, total = 0, 0
    
    for row in data_array:
        
        # the 0th index is the verb in question. Split between verb and meaning (separated by ':' in the data)
        # If there is no ':', then there is just no meaning to show.
        # (no .upper() here, it would turn ß into SS)
        if ':' in row[0]:
            verb, meaning = row[0].split(':', 1)
            print(prompt['Your verb is:'] + f' {cpr.BOLD}{verb.strip()}{cpr.END} ({cpr.ITALIC}{cpr.GREEN}{meaning.strip()}{cpr.END})')
        else:
            print(prompt['Your verb is:'] + f' {cpr.BOLD}{row[0]}{cpr.END}')
        # the remaining index are the other verb forms. We just loop through them.
        for ii in range(len(row)-1):
            # get question from header
            question = f'{cpr.symbol}{header_array[ii+1]}: '
            # get user input
            user_answer = input(question)
            # retrieve answer from answer array
            answer = f'[{cpr.ITALIC}{row[ii+1]}{cpr.END}]'
            # if its the example sentence, add in an extraline since they are usually long.
            if ii == (len(row) - 2):
                print('\033[1A\033[2K' + question + user_answer + '\n  ' + answer + '\n')
            else:
                # check the answer (the example sentence is not checked)
                total += 1
                if user_answer.strip().lower() == row[ii+1].lower():
                    correct += 1
                    mark = cpr.GREEN + '\u2713' + cpr.END
                else:
                    mark = cpr.RED + '\u2717' + cpr.END
                print('\033[1A\033[2K' + question + user_answer + ' ' + answer + ' ' + mark)
    # score
    if total > 0:
        print(prompt['You scored %s (%s%%).']%(str(correct), str(int(correct/total*100))))
    # end
    print('        ' + '\u2500'*8 + prompt["# End quiz #"] + '\u2500'*8)
