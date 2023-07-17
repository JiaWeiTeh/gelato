#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:52:59 2023

@author: Jia Wei Teh

This script contains the main tool for running the 'Artikel' mode.
"""

import pandas as pd
from tabulate import tabulate
import numpy as np
from functions import query

import artikel.artikel_functions as artikel_functions
    
def run(survival = False):
    # rerunning is by default False.
    isRerun = False
    # loop, because users have option to keep doing, or to exit.
    while True:
        # Import data
        data_csv = artikel_functions.load_file()
        dataframeObject = pd.DataFrame(data_csv)
        # Only show dictionary in the first run.
        if not isRerun:
            # Displaying the dataframe object
            pd.set_option('display.width', 500)
            # if users want to have a peek at the dictionary
            question_dictionary = 'Would you like to review the database before the quiz starts?'
            # defualt = 'yes'
            seeDict = query.yes_no(question_dictionary, 'no')
            # if yes, show.
            if seeDict:
                print('\nKlar! Here is a preview of your dictionary:\n')
                print(tabulate(dataframeObject, headers = ["Artikel", "Noun", "Translation", "Tag"], tablefmt = 'fancy_grid'))
        if survival:
            artikel_functions.qna_section(survival = True)
        else:
            # create QnA section
            artikel_functions.qna_section()
        # rerun?
        rerun_message = 'Congratulations! You have successfully completed the entire exercise. Would you like to redo the exercises?'
        isRerun = query.yes_no(rerun_message, 'no')
        # if not rerun, exit the program.
        if not isRerun:
            break
        
    return 



# TODO:s


# at the end show the time taken, show the accuracy.

# show how well you have done.

# if streak, then say you are in streak.

# for nounds, can allow users to pick from three meanins.