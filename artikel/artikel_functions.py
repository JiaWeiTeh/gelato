#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:05:11 2023

@author: Jia Wei Teh

This script contains functions that are used to run artikel.py
"""

import numpy as np
import pandas as pd

def load_file():
        
    # Reading an excel file
    excelFile = "./data/artikel.xlsx"
    excelFile = pd.read_excel(excelFile)
    # Update excel file into CSV file
    excelFile.to_csv("./data/artikel.csv", index = None, header=True)
    # Reading and Converting the output csv file into a dataframe object
    data_csv = pd.read_csv("./data/artikel.csv", skip_blank_lines = True, skiprows= [0], header = None)
    
    return data_csv


def qna_section():
    
    # read csv
    data_full = np.genfromtxt('./data/artikel.csv', delimiter=',', encoding="utf8", dtype = None)
    data_array = data_full[1:]
    header_array = data_full[0]
    # convert dictionary to list
    # get keys and values
    # randomise for QnA
    data_array = randomiser(data_array)
    # set number of questions
    questions, answers = data_array[:,1], data_array[:,0]
    questions, answers = set_number(questions, answers)
    # initialise list for wrong answers
    wrong_questions, wrong_answers = [], []
    print('   ' + '\u2500'*12 + "# Begin quiz #" + '\u2500'*12)
    print('Was ist der richtige Artikel für dieses Nomen?')

    incorrect_counter = True
    # loop through lists until all questions are answered correctly.
    while True:
        wrong_questions, wrong_answers = ask_questions(questions, answers, wrong_questions, wrong_answers)
        # Right after the first loop, record the wrong answers for analysis.
        # If nothing is wrong, finish.
        if not wrong_questions:
            if incorrect_counter:
                # calculate the score
                questions_right = int(len(questions) - len(wrong_questions))
                total_length = len(questions)
                precentage = int(questions_right/len(questions)*100)
            break
        else:
            # If something is wrong, run this part only once
            if incorrect_counter:
                # calculate the score
                questions_right = int(len(questions) - len(wrong_questions))
                total_length = len(questions)
                precentage = int(questions_right/len(questions)*100)
                # provide extra analysis
                analysis_message = get_analysis(wrong_questions, wrong_answers, data_array)
                # shutdown 
                incorrect_counter = False
                
            # update list into new ones
            questions, answers = wrong_questions, wrong_answers
            wrong_questions, wrong_answers = [], []
            # randomise again
            questions, answers = randomiser(np.array(questions), np.array(answers))
    # score
    print(f'You scored {questions_right}/{total_length} ({precentage}%).')
    if precentage != 100:
        print('Correct answers for parts where you got wrong:')
        print(analysis_message+"\033[39m")
    print('    ' + '\u2500'*12 + "# End quiz #" + '\u2500'*12)
    return



def get_analysis(wrong_questions, wrong_answers, data_array):
    
    message = ""
    # message for error answers
    for ii, (artikel, noun) in enumerate(list(zip(wrong_answers, wrong_questions))):
        # add meaning
        meaning = data_array[np.where(data_array[:,1] == wrong_questions)[0][0]][2]
        if ii == len(wrong_answers) - 1:
            message += "\033[33m" + artikel + " " + "\033[35m" + noun + "\033[39m (" + meaning + ")"
        else:
            message += "\033[33m" + artikel + " " + "\033[35m" + noun + "\033[39m (" + meaning + ")\n"
    
    return message


def set_number(questions, answers):
    
    # what is the maximum questions allowed?
    max_questions = len(questions)
    # what does the user want?
    user_number = input('Provide the number of questions for your quiz: ')
    # error-proofing
    while True:
        try:
            int(user_number)
            break
        except:
            user_number = input('Input invalid. Please enter a number: ')
            
    user_number = int(user_number)
    # case if user provides too large of a value
    if user_number > max_questions:
        print(f'Number exceeds maximum rows in provided wordbase (max = {max_questions}). Set number of questions to max.')
        user_number = max_questions
    # from user's input, cut down the list.
    questions = questions[:user_number]
    answers = answers[:user_number]
    
    return questions, answers


def ask_questions(questions, answers, wrong_questions, wrong_answers):

    # basic form of query 
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
            print('\033[1A\033[2K' + q + ': ' + user_answer + ' (Incorrect)')
            # special case if it is the last index, stop query.
            if (ii+1) == len(questions):
                return wrong_questions, wrong_answers
            else:
                query = questions[ii+1] + ': '
            
    return wrong_questions, wrong_answers


def randomiser(*args):
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




