#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:52:59 2023

@author: Jia Wei Teh
"""

import pandas as pd
from tabulate import tabulate
from functions import query

import artikel.artikel_functions as artikel_functions
    
def run():
    
    # loop, because users have option to keep doing, or to exit.
    while True:
        # Import data
        dataframeObject = artikel_functions.load_file()
        # Displaying the dataframe object
        pd.set_option('display.width', 500)
        # if users want to have a peek at the dictionary
        question_dictionary = '\nDisplay wordbase before quiz begins?'
        # defualt = 'yes'
        seeDict = query.yes_no(question_dictionary, 'no')
        # if yes, show.
        if seeDict:
            print('\nKlar! Here is a glimpse of your dictionary:\n')
            print(tabulate(dataframeObject, headers = dataframeObject.columns, tablefmt = 'fancy_grid'))
        # create QnA section
        artikel_functions.qna_section(dataframeObject)
        # rerun?
        rerun_message = 'Congratulations! You have completed the full exercise correctly. Re-do the exercises?'
        isRerun = query.yes_no(rerun_message, 'no')
        # if not rerun, exit the program.
        if not isRerun:
            break
        
    return 



# TODO:s

# if correct, dont show again.
# if wrong, show again, but not immediately after. if it is the last, 
# then get a random one/ up to 3, then show it again.

# ability to set how many questions you will be asked.

# at the end show the time taken, show the accuracy.

# show how well you have done.

# if streak, then say you are in streak.


# for nounds, can allow users to pick from three meanins.