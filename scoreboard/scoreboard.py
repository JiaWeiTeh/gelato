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
from functions.common import DATA_DIR


def show_scoreboard(fname='artikel'):

    # Reading and Converting the output csv file into a dataframe object
    score_csv = pd.read_csv(DATA_DIR / f"{fname}_scoreboard.csv", header=None)

    # Displaying the dataframe object
    pd.set_option('display.width', 500)
    print(prompt["Here are the top three high scores:"])
    print(tabulate(score_csv, headers=[prompt["Score"], prompt["User"], prompt["Date"]], tablefmt='fancy_grid', showindex=False))


def update_scoreboard(currentScore, fname='artikel'):
    # time today
    today = date.today()
    scoreboard_path = DATA_DIR / f"{fname}_scoreboard.csv"
    # if file is not empty, then this try block will fail.
    try:
        df = pd.read_csv(scoreboard_path, header=None)
        top_names = list(df[1])
        top_scores = list(map(lambda x: int(x.replace(" pts", "")), df[0]))
        top_times = list(df[2])

        if np.where(currentScore > np.array(top_scores))[0].size > 0 or len(top_scores) < 3:
            name = ask_name()
            newpair = (currentScore, name, today.strftime("%d/%m/%Y"))
            update = list(zip(top_scores, top_names, top_times))
            update.append(newpair)
            update = sorted(update)[::-1][:3]

            with open(scoreboard_path, "w") as output:
                writer = csv.writer(output)
                for (score, name, time) in update:
                    writer.writerow([str(score)+" pts", name, time])

    # if file is empty or malformed
    except (FileNotFoundError, KeyError, IndexError, pd.errors.EmptyDataError):
        name = ask_name()
        with open(scoreboard_path, "w") as output:
            writer = csv.writer(output)
            writer.writerow([str(currentScore)+" pts", name, today.strftime("%d/%m/%Y")])


def ask_name():

    # Ask for username, but make sure it has a length limit!
    while True:
        username = input(prompt["Congratulations on achieving a high score! Please enter your username: "]).strip()
        if len(username) == 0:
            print("Username cannot be empty. Please try again.")
        elif len(username) > 10:
            print(prompt["Your username exceeds the maximum length of 10 characters. Please try again."])
        else:
            break

    return username
