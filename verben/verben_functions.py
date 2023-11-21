#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:17:53 2023

@author: Jia Wei Teh

This script contains functions that are used to run verben.py
"""

import numpy as np
import pandas as pd
from language.dictionary import prompt
from functions.terminal_prints import cprint as cpr


# TODO:
    # add prompts
    # add functionality to guess the blank in a sentence.


def load_file():
        
    # Reading an excel file
    excelFile = "./data/verben.xlsx"
    excelFile = pd.read_excel(excelFile)
    # Update excel file into CSV file
    excelFile.to_csv("./data/verben.csv", index = None, header=True)
    # Reading and Converting the output csv file into a dataframe object
    data_csv = pd.read_csv("./data/verben.csv", skip_blank_lines = True, skiprows= [0], header = None)
    return data_csv


def qna_section(config, survival):
    
    # read csv
    data_full = np.genfromtxt('./data/verben.csv', 
                               delimiter='\t',
                              encoding="utf8", dtype = None)
    data_array_temporary = data_full[1:]
    # needs split because our delimiter was '\t'.
    header_array = data_full[0].split(',')
    
    # Now, ideally we would like to split the data into different columns.
    # However, since we are dealling with strings, that means sentences may 
    # include ',' characters. Since we have hardcoded that the sentences must 
    # be at the last columnm, we can simply say that whatever is past a certain column
    # has to all concatenate. Here is exactly what is happening.
    
    # declare array
    data_array = np.ones((len(data_array_temporary), len(header_array)), dtype = object)
    
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
            
    # convert dictionary to list
    # get keys and values
    
    # randomise for QnA, plus set the number of questions
    data_array = set_number(randomiser(data_array))
    
    print('       ' + '\u2500'*8 + "# Begin quiz #" + '\u2500'*8 + '\n')
    
    for row in data_array:
        
        # the 0th index is the verb in question.
        print(f'Your verb is: {cpr.BOLD}{row[0].upper()}{cpr.END}')
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
                
    print('        ' + '\u2500'*8 + "# End quiz #" + '\u2500'*8)


def set_number(data_array, config):
    # TODO: add def number
    
    # what is the maximum questions allowed?
    max_questions = len(data_array)
    # what does the user want?
    user_number = input(prompt['Please indicate the number of questions for your quiz: '])
    # error-proofing
    while True:
        try:
            int(user_number)
            break
        except:
            user_number = input(prompt['The input is invalid. Please enter a valid number: '])
            
    user_number = int(user_number)
    # case if user provides too large of a value
    if user_number > max_questions:
        print(prompt['The number of questions exceeds the maximum allowable rows in the provided wordbase (maximum = %s).\nWe will now set the number of questions to the maximum limit.']%str(max_questions))
        user_number = max_questions
    # from user's input, cut down the list.
    return data_array[:user_number]



def randomiser(*args):
    # Hardcoded - accepts only either the entire DataFrame, or a question-answer tuple.
    # randomise indices
    if len(args) == 1:
        array = args[0]
        indices = np.arange(array.shape[0])
        np.random.shuffle(indices)
        # re-order array with indices
        array = array[indices]
        return array
    else:
        questions, answers = args
        indices = np.arange(questions.shape[0])
        np.random.shuffle(indices)
        # re-order array with indices
        questions = questions[indices]
        answers = answers[indices]
        return questions, answers        




