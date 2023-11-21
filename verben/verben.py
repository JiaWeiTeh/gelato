#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:15:30 2023

@author: Jia Wei Teh

This script contains the main tool for running the 'Verben' mode.
"""

import pandas as pd
from tabulate import tabulate
from functions import query
from language.dictionary import prompt
import verben.verben_functions as verben_functions
    
def run(config, survival):
    # rerunning is by default False.
    isRerun = False
    # loop, because users have option to keep doing, or to exit.
    while True:
        # Import data
        data_csv = verben_functions.load_file()
        dataframeObject = pd.DataFrame(data_csv)
        # Only show dictionary in the first run.
        if not isRerun:
            # Displaying the dataframe object
            pd.set_option('display.width', 500)
            # if users want to have a peek at the dictionary
            question_dictionary = prompt['Would you like to review the database before the quiz starts?']
            # defualt = 'yes'
            seeDict = query.yes_no(question_dictionary, 'no')
            # if yes, show.
            if seeDict:
                print(prompt['\nHere is a preview of your dictionary:\n'])
                print(tabulate(dataframeObject, headers = ["Infinitiv", "Präsens", "Präteritum", "Perfekt", "Beispielsatz"], tablefmt = 'fancy_grid'))
        if survival:
            verben_functions.qna_section(config, survival = True)
        else:
            # create QnA section
            verben_functions.qna_section(config, survival = False)
        # rerun?
        rerun_message = prompt['Congratulations! You have successfully completed the entire exercise. Would you like to redo the exercises?']
        isRerun = query.yes_no(rerun_message, 'no')
        # if not rerun, exit the program.
        if not isRerun:
            break
        
    return 


