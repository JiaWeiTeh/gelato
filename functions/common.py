#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Common utility functions shared across quiz modes (artikel, verben, etc.).
"""

from pathlib import Path
import numpy as np
import pandas as pd
from language.dictionary import prompt

# Project root directory (parent of the 'functions' package)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"


def load_excel(filename):
    """Load an Excel file from the data directory and return a DataFrame.

    Also exports a CSV to the data directory so that downstream numpy-based
    readers (qna_section) can consume it via np.genfromtxt.
    """
    filepath = DATA_DIR / filename
    csv_name = filepath.stem + ".csv"
    csv_path = DATA_DIR / csv_name
    df = pd.read_excel(filepath)
    df.to_csv(csv_path, index=None, header=True)
    # Return without the header row, matching the original skiprows=[0], header=None behavior
    data_csv = pd.DataFrame(df.values)
    return data_csv


def randomiser(*args):
    """Shuffle array(s) in unison using random index permutation.

    Accepts either:
      - A single 2D array: returns the shuffled array.
      - Two 1D arrays (questions, answers): returns both shuffled in unison.
    """
    if len(args) == 1:
        array = args[0]
        indices = np.arange(array.shape[0])
        np.random.shuffle(indices)
        return array[indices]
    else:
        questions, answers = args
        indices = np.arange(questions.shape[0])
        np.random.shuffle(indices)
        return questions[indices], answers[indices]


def set_number_single(data_array, config):
    """Prompt user for number of questions and slice a single data array.

    Used by verben mode where questions/answers are in one array.
    """
    max_questions = len(data_array)
    user_number = _ask_number_of_questions(max_questions)
    return data_array[:user_number]


def set_number_pair(questions, answers, config):
    """Prompt user for number of questions and slice parallel arrays.

    Used by artikel mode where questions and answers are separate arrays.
    """
    max_questions = len(questions)
    user_number = _ask_number_of_questions(max_questions)
    return questions[:user_number], answers[:user_number]


def _ask_number_of_questions(max_questions):
    """Shared input logic: ask user for a valid positive integer, capped at max."""
    user_number = input(prompt['Please indicate the number of questions for your quiz: '])
    while True:
        if user_number == "":
            print('No input detected.')
            user_number = max_questions
            break
        else:
            try:
                user_number = int(user_number)
                if user_number <= 0:
                    raise ValueError
                break
            except ValueError:
                user_number = input(prompt['The input is invalid. Please enter a valid number: '])

    user_number = int(user_number)
    if user_number >= max_questions:
        print(f'We will set the number of questions to the maximum limit. (maximum = {max_questions})')
        user_number = max_questions
    return user_number
