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


def qna_section(config):

    # Read each line as a single string (delimiter='\t' acts as "no split"
    # since the CSV has no tab characters). We split manually below because
    # the last column (example sentence) may contain commas.
    data_full = np.genfromtxt(DATA_DIR / "verben.csv",
                              delimiter='\t',
                              encoding="utf8", dtype=None)
    header_array = data_full[0].split(',')
    data_array_temporary = data_full[1:]

    # Split each row by comma, merging trailing fields into the last
    # column to handle commas within example sentences.
    num_cols = len(header_array)
    data_array = np.ones((len(data_array_temporary), num_cols), dtype=object)

    for ii in range(len(data_array)):
        fields = data_array_temporary[ii].split(',')
        if len(fields) > num_cols:
            data_array[ii][:num_cols-1] = fields[:num_cols-1]
            data_array[ii][-1] = ','.join(fields[num_cols-1:]).replace('"', '')
        else:
            data_array[ii] = fields

    # randomise for QnA, plus set the number of questions
    data_array = set_number_single(randomiser(data_array), config)

    # begin
    print('       ' + '\u2500'*8 + "# Begin quiz #" + '\u2500'*8 + '\n')

    total_fields = 0
    correct_fields = 0

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
            correct_answer = row[ii+1].strip()
            answer_display = f'[{cpr.ITALIC}{correct_answer}{cpr.END}]'

            # check correctness (skip example sentences — last field)
            is_example = (ii == len(row) - 2)
            if not is_example:
                total_fields += 1
                if user_answer.strip().lower() == correct_answer.lower():
                    correct_fields += 1
                    mark = f'{cpr.GREEN}\u2713{cpr.END}'
                else:
                    mark = f'{cpr.RED}\u2717{cpr.END}'
                print('\033[1A\033[2K' + question + user_answer + ' ' + answer_display + ' ' + mark)
            else:
                # example sentence — just show the answer
                print('\033[1A\033[2K' + question + user_answer + '\n  ' + answer_display + '\n')

    # score summary
    if total_fields > 0:
        percentage = int(correct_fields / total_fields * 100)
        print(prompt['You scored %s (%s%%).'] % (str(correct_fields), str(percentage)))

    # end
    print('        ' + '\u2500'*8 + "# End quiz #" + '\u2500'*8)
