#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:28:14 2023

@author: Jia Wei Teh
"""


import pandas as pd
from tabulate import tabulate
from functions import query

import artikel.artikel_functions as artikel_functions
    
def run():
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
            question_dictionary = 'Display wordbase before quiz begins?'
            # defualt = 'yes'
            seeDict = query.yes_no(question_dictionary, 'no')
            # if yes, show.
            if seeDict:
                print('\nKlar! Here is a glimpse of your dictionary:\n')
                print(tabulate(dataframeObject, headers = dataframeObject.columns, tablefmt = 'fancy_grid'))
        # create QnA section
        artikel_functions.qna_section()
        # rerun?
        rerun_message = 'Congratulations! You have completed the full exercise. Re-do the exercises?'
        isRerun = query.yes_no(rerun_message, 'no')
        # if not rerun, exit the program.
        if not isRerun:
            break
        
    return 
