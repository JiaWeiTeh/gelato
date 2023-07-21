#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:54:50 2023

@author: Jia Wei Teh
"""


import numpy as np
import pandas as pd
import csv
from tabulate import tabulate
from datetime import date



def scoreboard(username, score):
    
    

    return


def record_score(name, score):
    
    # time
    today = date.today()
    # write into csv file
    with open("./data/scoreboard.csv", "a") as output:
        writer = csv.writer(output)
        writer.writerow([name, str(score)+" pts", today.strftime("%d/%m/%Y")])
    
    return


def show_scoreboard():
    
    # Reading and Converting the output csv file into a dataframe object
    score_csv = pd.read_csv("./data/scoreboard.csv")
 
    # Displaying the dataframe object
    pd.set_option('display.width', 500)
    # if users want to have a peek at the dictionary
    # question_dictionary = 'Would you like to review the database before the quiz starts?'
    # default = 'yes'
    # seeScore = query.yes_no(question_dictionary, 'no')
    # if yes, show.
    print(tabulate(score_csv, headers = ["Player", "Score", "Date"], tablefmt = 'fancy_grid'))
    
    return

def check_top5(name, currentScore):
    
    highscore = False
    # name 
    top_names = list(list(pd.read_csv("./data/scoreboard.csv", header = None).items())[0][1])
    # top score
    top_scores = list(pd.read_csv("./data/scoreboard.csv", header = None).items())[1][1]
    # pure score
    top_scores = list(map(lambda x: int(x.replace(" pts", "")), top_scores))
    # tuple
    pairs = list(zip(top_names, top_scores))
    
    return pairs


print(check_top5('top', 5))






    