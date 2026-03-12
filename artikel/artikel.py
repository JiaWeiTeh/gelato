#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:52:59 2023

@author: Jia Wei Teh

This script contains the main tool for running the 'Artikel' mode.
"""

import pandas as pd
from tabulate import tabulate
from functions import query
from language.dictionary import prompt
import artikel.artikel_functions as artikel_functions


def run(config, survival):
    # rerunning is by default False.
    is_rerun = False
    # loop, because users have option to keep doing, or to exit.
    while True:
        # Import data
        data_csv = artikel_functions.load_file()
        df = pd.DataFrame(data_csv)
        # Only show dictionary in the first run.
        if not is_rerun:
            # Displaying the dataframe object
            pd.set_option('display.width', 500)
            # if users want to have a peek at the dictionary
            question_dictionary = prompt['Review database before quiz starts?']
            see_dict = query.yes_no(question_dictionary, 'no')
            # if yes, show.
            if see_dict:
                print(prompt['\nHere is a preview of your dictionary:\n'])
                print(tabulate(df, headers=["Artikel", "Noun", "Translation", "Tag"], tablefmt='fancy_grid'))
        # written in if-else just for clarity.
        if survival:
            artikel_functions.qna_section(config, survival=True)
        else:
            artikel_functions.qna_section(config, survival=False)
        # rerun?
        rerun_message = prompt['Congratulations! You have successfully completed the entire exercise. Would you like to redo the exercises?']
        is_rerun = query.yes_no(rerun_message, 'no')
        # if not rerun, exit the program.
        if not is_rerun:
            break
