#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:17:53 2023

@author: Jia Wei Teh

This script contains functions that are used to run verben.py
"""

import numpy as np
from language.dictionary import prompt
from functions.terminal_prints import cprint as cpr
from functions.common import load_excel, randomiser, set_number_single, DATA_DIR


# TODO:
    # add prompts
    # add functionality to guess the blank in a sentence.


def load_file():
    return load_excel("verben.xlsx")


def qna_section(config, survival):

    # read csv
    data_full = np.genfromtxt(DATA_DIR / "verben.csv",
                               delimiter='\t',
                              encoding="utf8", dtype=None)
    data_array_temporary = data_full[1:]
    # needs split because our delimiter was '\t'.
    header_array = data_full[0].split(',')

    # Now, ideally we would like to split the data into different columns.
    # However, since we are dealling with strings, that means sentences may
    # include ',' characters. Since we have hardcoded that the sentences must
    # be at the last columnm, we can simply say that whatever is past a certain column
    # has to all concatenate. Here is exactly what is happening.

    # declare array
    data_array = np.ones((len(data_array_temporary), len(header_array)), dtype=object)

    for ii in range(len(data_array)):
        # check if there is more than allowed collumns
        if len(data_array_temporary[ii].split(',')) > len(header_array):
            # everything until the column before last stays the same
            data_array[ii][:len(header_array)-1] = data_array_temporary[ii].split(',')[:len(header_array)-1]
            # the last row, concatenate the rest
            data_array[ii][-1] = ','.join(data_array_temporary[ii].split(',')[len(header_array)-1:])
            # cleaning since there are '"' characters sometimes.
            data_array[ii][-1] = data_array[ii][-1].replace('"', '')
        else:
            data_array[ii] = data_array_temporary[ii].split(',')

    # randomise for QnA, plus set the number of questions
    data_array = set_number_single(randomiser(data_array), config)

    # begin
    print('       ' + '\u2500'*8 + "# Begin quiz #" + '\u2500'*8 + '\n')

    for row in data_array:

        # the 0th index is the verb in question. Split between verb and meaning (separated by ':' in the data)
        verb, meaning = row[0].split(':')

        print(f'Your verb is: {cpr.BOLD}{verb.upper()}{cpr.END} ({cpr.ITALIC}{cpr.GREEN}{meaning}{cpr.END})')
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
                print('\033[1A\033[2K' + question + user_answer + ' ' + answer)
    # end
    print('        ' + '\u2500'*8 + "# End quiz #" + '\u2500'*8)
