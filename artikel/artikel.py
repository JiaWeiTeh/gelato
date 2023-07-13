#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:52:59 2023

@author: Jia Wei Teh
"""

import pandas as pd
from tabulate import tabulate
from functions import query
import numpy as np
import os
import time
import sys

def run():
    
    dataframeObject = load_file()

    # Displaying the dataframe object
    pd.set_option('display.width', 500)

    question_dictionary = 'Do you want to have a look at your wordbase before the quiz?'
    
    seeDict = query.yes_no(question_dictionary, 'yes')
    
    if seeDict:
        print('\nKlar! Here is a glimpse of your dictionary:\n')
        print(tabulate(dataframeObject, headers = dataframeObject.columns, tablefmt = 'fancy_grid'))
    
    qna_section(dataframeObject)
    
    print('Congratulations! You have completed the full exercise correctly.')
    
    return 



def load_file():
    
        
    path2work = r'/Users/jwt/Documents/Code/gelato/artikel'
    os.chdir(path2work)
    
    excelFile = "artikel.xlsx"
    
    # Reading an excel file
    excelFile = pd.read_excel(excelFile)
    
    # Update excel file into CSV file
    excelFile.to_csv("artikel.csv", index = None, header=True)
    
    # Reading and Converting the output csv file into a dataframe object
    dataframeObject = pd.DataFrame(pd.read_csv("artikel.csv", skiprows = [1]))
    
    
    return dataframeObject



def qna_section(dataframeObject):
    
    dictionary = dataframeObject.to_dict('list')
    
    questions = np.array(dictionary['Noun'])
    answers = np.array(dictionary['Artikel'])
    questions, answers = randomiser(questions, answers)
    
    questions, answers = set_number(questions, answers)
    wrong_questions, wrong_answers = [], []

    print('\nWas ist der richtige Artikel für dieses Nomen?\n')

    while True:
        wrong_questions, wrong_answers = ask_questions(questions, answers, wrong_questions, wrong_answers)
        if wrong_questions:
            questions, answers = wrong_questions, wrong_answers
            wrong_questions, wrong_answers = [], []
        else:
            break
        
    return


def set_number(questions, answers):
    
    max_questions = len(questions)
    
    user_number = int(input('\nProvide the number N of questions for your quiz: '))
    
    if user_number > max_questions:
        print(f'Number provided exceeds the available rows ({max_questions}) in wordbase. Set N = {max_questions}')
        user_number = max_questions
        
    questions = questions[:user_number]
    answers = answers[:user_number]
    
    return questions, answers



def ask_questions(questions, answers, wrong_questions, wrong_answers):
    
    
    query = questions[0] + ': '
    
    for ii, q in enumerate(questions):
        
        user_answer = input(query).replace(" ","")
        
        # if the answer is correct, overwrite the NEXT question on the same line
        if user_answer == answers[ii].replace(" ",""):
            # special case if it is the last index, stop query.
            if (ii+1) == len(questions):
                print('\033[1A\033[2K\033[1A')
                return wrong_questions, wrong_answers
            # if there is no overflow, overwrite with new query.
            else:
                query = '\033[1A\033[2K' + questions[ii+1] + ': '
        # if the answer is wrong, delete the query and reprint with incorrect.
        else:
            # record wrong pairs
            wrong_questions.append(questions[ii])
            wrong_answers.append(answers[ii])
            # special case if it is the last index, stop query.
            if (ii+1) == len(questions):
                print('\033[1A\033[2K'+ q + ': ' + user_answer + ' (Incorrect)')
                return wrong_questions, wrong_answers
            else:
                print('\033[1A\033[2K'+ q + ': ' + user_answer + ' (Incorrect)')
                query = questions[ii+1] + ': '
            
    return wrong_questions, wrong_answers
    


def randomiser(questions, answers):
    
    indices = np.arange(questions.shape[0])
    np.random.shuffle(indices)
    
    questions = questions[indices]
    answers = answers[indices]
    
    return questions, answers


#  problem, when list ias of length 1, it does not show (incorrect).








# TODO:s

# if correct, dont show again.
# if wrong, show again, but not immediately after. if it is the last, 
# then get a random one/ up to 3, then show it again.

# ability to set how many questions you will be asked.

# at the end show the time taken, show the accuracy.

# show how well you have done.

# if streak, then say you are in streak.


# print last modified time of excel
        
        # import os                                                                   
        # import glob             
        
        # excel_folder = 'C:/Users/ThisOne/ExcelStuff/'
        
        # # glob.glob returns all paths matching the pattern.
        # excel_files = list(glob.glob(os.path.join(excel_folder, '*.xls*')))
        
        # mod_dates = [os.path.getmtime(f) for f in excel_files]
        
        # # sort by mod_dates.
        # file_date = zip(excel_files, mod_dates).sort(key=lambda d: d[1])
        
        # newest_file_path = file_date[0][1]


# for nounds, can allow users to pick from three meanins.