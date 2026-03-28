#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:05:11 2023

@author: Jia Wei Teh

This script contains functions that are used to run artikel.py
"""

import numpy as np
from scoreboard import scoreboard
from language.dictionary import prompt
from functions import footer
from functions.common import load_excel, randomiser, set_number_pair, DATA_DIR


def load_file():
    return load_excel("artikel.xlsx")


def qna_section(config, survival):

    # read data directly from Excel via numpy for the QnA array
    data_full = np.genfromtxt(DATA_DIR / "artikel.csv", delimiter=',', encoding="utf8", dtype=None)
    data_array = data_full[1:]
    # randomise for QnA
    data_array = randomiser(data_array)
    # set number of questions
    questions, answers = data_array[:, 1], data_array[:, 0]

    # enter survival mode. Default is 3 lives.
    if survival:
        current_hearts = int(config.artikel_challenge.hearts)
        if current_hearts <= 0:
            current_hearts = 3
        elif current_hearts > 10:
            current_hearts = 10
        print('       ' + '\u2500'*8 + "# Begin quiz #" + '\u2500'*8 + '\n')
        print(prompt['What are the correct articles for these nouns? [der/die/das]'])
        # survival score
        survival_score = 0
        analysis_message = ""

        # initialise array for wrong answers
        wrong_questions, wrong_answers = [], []
        # ask questions
        wrong_questions, wrong_answers, current_hearts, questions_answered = ask_question_survival(questions, answers, wrong_questions, wrong_answers, current_hearts, current_hearts)
        # update score. You have either completed the entire challenge or have used up all your hearts.
        survival_score = questions_answered - len(wrong_answers)
        # analysis
        current_analysis = get_analysis(wrong_questions, wrong_answers, data_array)
        analysis_message += current_analysis
        # if finished challenge with hearts remaining, win the game.
        if current_hearts > 0:
            footer.win()
            print(prompt['You have successfully answered %s questions correctly!'] % str(survival_score))
            print('Congratulations.')
            scoreboard.update_scoreboard(survival_score)
            scoreboard.show_scoreboard()
            print('        ' + '\u2500'*8 + "# End quiz #" + '\u2500'*8)
        elif current_hearts == 0:
            # score
            print(prompt['You have successfully answered %s questions correctly!'] % str(survival_score))
            scoreboard.update_scoreboard(survival_score)
            scoreboard.show_scoreboard()
            print(prompt['Here are the correct answers for the part(s) where you\'ve made mistake(s):'])
            print(analysis_message)
            print('        ' + '\u2500'*8 + "# End quiz #" + '\u2500'*8)

    elif not survival:
        questions, answers = set_number_pair(questions, answers, config)
        # initialise list for wrong answers
        wrong_questions, wrong_answers = [], []
        print('       ' + '\u2500'*8 + prompt["# Begin quiz #"] + '\u2500'*8)
        print(prompt['What are the correct articles for these nouns? [der/die/das]'])

        incorrect_counter = True
        questions_right = len(questions)
        percentage = 100
        analysis_message = ""
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
                    percentage = int(questions_right / len(questions) * 100)
                break
            else:
                # If something is wrong, run this part only once
                if incorrect_counter:
                    # calculate the score
                    questions_right = int(len(questions) - len(wrong_questions))
                    total_length = len(questions)
                    percentage = int(questions_right / total_length * 100)
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
        print(prompt['You scored %s (%s%%).'] % (str(questions_right), str(percentage)))
        if percentage != 100:
            print(prompt['Here are the correct answers for the part(s) where you\'ve made mistake(s):'])
            print(analysis_message)
        else:
            footer.win()
        print('        ' + '\u2500'*8 + prompt["# End quiz #"] + '\u2500'*8)



def get_analysis(wrong_questions, wrong_answers, data_array):

    message = ""
    # message for error answers
    for ii, (artikel, noun) in enumerate(list(zip(wrong_answers, wrong_questions))):
        # add translation
        translation = data_array[np.where(data_array[:, 1] == wrong_questions[ii])[0][0]][2]
        message += "\033[33m{:<4}\033[35m{:<20}\033[39m{:<20}\033[39m\n".format(artikel, noun, "["+translation+"]")

    return message


def ask_questions(questions, answers, wrong_questions, wrong_answers):

    # basic form of query
    query = questions[0] + ': '

    for ii, q in enumerate(questions):

        user_answer = input(query).replace(" ", "")

        # if the answer is correct, overwrite the NEXT question on the same line
        if user_answer == answers[ii].replace(" ", ""):
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
            print('\033[1A\033[2K' + q + ': ' + user_answer + ' {:<20}'.format(prompt['(Incorrect)']))
            # special case if it is the last index, stop query
            if (ii+1) == len(questions):
                return wrong_questions, wrong_answers
            else:
                query = questions[ii+1] + ': '

    return wrong_questions, wrong_answers


def ask_question_survival(questions, answers, wrong_questions, wrong_answers, hearts, max_hearts):

    # current hearts
    current_hearts = hearts

    # basic form of query
    query = print_hearts(max_hearts, current_hearts) + questions[0] + ': '

    questions_answered = 0
    for index, q in enumerate(questions):
        # don't ask questions once no more hearts left.
        if current_hearts <= 0:
            break
        else:
            questions_answered += 1
            hearts_status = print_hearts(max_hearts, current_hearts)
            user_answer = input(query).replace(" ", "")
            # if the answer is correct, overwrite the NEXT question on the same line
            if user_answer == answers[index].replace(" ", ""):
                # special case if it is the last index, stop query.
                if (index+1) == len(questions):
                    print('\033[1A\033[2K\033[1A')
                    return wrong_questions, wrong_answers, current_hearts, questions_answered
                # if there is no overflow, overwrite with new query.
                else:
                    query = '\033[1A\033[2K' + hearts_status + questions[index+1] + ': '
            # if the answer is wrong, delete the query and reprint with incorrect.
            else:
                current_hearts -= 1
                # record wrong pairs
                wrong_questions.append(questions[index])
                wrong_answers.append(answers[index])
                print('\033[1A\033[2K' + hearts_status + q + ': ' + user_answer + ' ' + prompt['(Incorrect)'])
                # special case if it is the last index, stop query.
                if (index+1) == len(questions):
                    return wrong_questions, wrong_answers, current_hearts, questions_answered
                # otherwise, next query.
                else:
                    hearts_status = print_hearts(max_hearts, current_hearts)
                    query = hearts_status + questions[index+1] + ': '

    return wrong_questions, wrong_answers, current_hearts, questions_answered



def print_hearts(max_hearts, current_hearts):

    filled_heart = "\u2665 "
    empty_heart = "\u2661 "
    # how many filled hearts?
    hearts = empty_heart * (max_hearts - current_hearts) + filled_heart * current_hearts + '   '

    return hearts
