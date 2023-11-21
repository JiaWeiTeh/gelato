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
from language.dictionary import prompt


def show_scoreboard(fname = 'artikel'):
    
    # Reading and Converting the output csv file into a dataframe object
    score_csv = pd.read_csv(f"./data/{fname}_scoreboard.csv", header = None)
 
    # Displaying the dataframe object
    pd.set_option('display.width', 500)
    # if users want to have a peek at the dictionary
    # question_dictionary = 'Would you like to review the database before the quiz starts?'
    # default = 'yes'
    # seeScore = query.yes_no(question_dictionary, 'no')
    # if yes, show.
    print(prompt["Here are the top three high scores:"])
    print(tabulate(score_csv, headers = [prompt["Score"], prompt["User"], prompt["Date"]], tablefmt = 'fancy_grid', showindex = False))
    
    return

# TODO: THIS IS LAZY. PLEASE IMPLEMENT PARAMETER INSTEAD OF PUT DEFAULT VALUE.
def update_scoreboard(currentScore, fname = 'artikel'):
    # time today
    today = date.today()
    # if file is not empty
    try:
        # name 
        top_names = np.array(list(list(pd.read_csv(f"./data/{fname}_scoreboard.csv", header = None).items())[1][1]))
        # top score
        top_scores = list(pd.read_csv(f"./data/{fname}_scoreboard.csv", header = None).items())[0][1]
        # pure score
        top_scores = list(map(lambda x: int(x.replace(" pts", "")), top_scores))
        # top time
        top_times = list(pd.read_csv(f"./data/{fname}_scoreboard.csv", header = None).items())[2][1]
        
        if np.where(currentScore > np.array(top_scores))[0].size > 0 or len(top_scores) < 3:
            name = ask_name()
            newpair = (currentScore, name, today.strftime("%d/%m/%Y"))
            update = list(zip(top_scores, top_names, top_times))
            update.append(newpair)
            update = sorted(update)[::-1][:3]
            
            with open(f"./data/{name}_scoreboard.csv", "w") as output:
                writer = csv.writer(output)
                for (score, name, time) in update:
                    writer.writerow([str(score)+" pts", name, time])
                    
        elif len(top_scores) < 3:
            return
        
    # if file is empty
    except:
        name = ask_name()
        with open(f"./data/{fname}_scoreboard.csv", "w") as output:
            writer = csv.writer(output)
            writer.writerow([str(currentScore)+" pts", name, today.strftime("%d/%m/%Y")])
    
    return 


def ask_name():
    
    # Ask for username, but make sure it has a length limit!
    while True:
        username = input(prompt["Congratulations on achieving a high score! Please enter your username: "])
        if len(username) > 10:
            print(prompt["Your username exceeds the maximum length of 10 characters. Please try again."])
        else:
            break
    
    return username






    