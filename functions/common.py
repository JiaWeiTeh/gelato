#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:01:52 2026

@author: Jia Wei Teh

This script contains functions that are shared between the quiz modes.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from language.dictionary import prompt

# the folder where gelato lives, so that it also works when called from elsewhere.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"


def load_excel(filename):

    # Reading an excel file
    df = pd.read_excel(DATA_DIR / filename)
    # empty cells are NaN, we just want empty strings.
    df = df.fillna('').astype(str)
    # remove stray spaces, e.g. 'die ' instead of 'die'. Same for the headers.
    df.columns = [str(col).strip() for col in df.columns]
    for col in df.columns:
        df[col] = df[col].str.strip()

    return df


def set_number(max_questions, default=None):

    # if nothing is set in settings.yml, pressing enter gives the maximum.
    if default is None:
        default = max_questions
    # what does the user want?
    user_number = input(prompt['Please indicate the number of questions for your quiz: '])
    # error-proofing
    while True:
        # if nothing, set as default
        if user_number == "":
            print(prompt['No input detected. Using %s questions.'] % str(min(default, max_questions)))
            user_number = default
            break
        else:
            try:
                user_number = int(user_number)
                if user_number <= 0:
                    raise ValueError
                break
            except ValueError:
                user_number = input(prompt['The input is invalid. Please enter a valid number: '])

    # case if user provides too large of a value
    if user_number > max_questions:
        print(prompt['We will set the number of questions to the maximum limit. (maximum = %s)'] % str(max_questions))
        user_number = max_questions

    return user_number


def randomiser(*args):
    # Hardcoded - accepts only either the entire array, or a question-answer tuple.
    # randomise indices
    if len(args) == 1:
        array = args[0]
        indices = np.arange(array.shape[0])
        np.random.shuffle(indices)
        # re-order array with indices
        return array[indices]
    else:
        questions, answers = args
        indices = np.arange(questions.shape[0])
        np.random.shuffle(indices)
        # re-order array with indices
        return questions[indices], answers[indices]
