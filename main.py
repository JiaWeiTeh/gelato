#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:52:44 2023

@author: Jia Wei Teh

This is the main file, which the user can change modes. 
"""


from artikel import artikel
import functions.header as header
import time
import sys

header.display()
modes_dict = {'1': 'Artikel',
              '2': 'Nouns',
              '0': 'Exit'
              }
for key, value in modes_dict.items():
    print('\t\t'+str(key)+':', value)
print('\t\t--------------------------------------------------')

input_mode = input('\n\nPlease enter your desired number: ').replace(" ", "")
time.sleep(.25)

if input_mode in list(modes_dict.keys()):
    true_mode = modes_dict[input_mode]
    modeExist = True
else:
    modeExist = False

message = '\nEntering the \"'
if modeExist:
    if input_mode == '1':
        print(message+true_mode+'\" mode....\n')
        time.sleep(.75)
        artikel.run()
    elif input_mode == '2':
        print('Woops! Section TBD.')
    elif input_mode == '0':
        sys.exit('Program ended.')
else:
    print(f'Mode \"{input_mode}\" not recognised. Ending program!')

print('Exiting GELATO...')


# TODO: make this into shell script, to include italics and colours.
# e.g., make main.sh that will run when gelato is typed in terminal.
# then, use bash print functions, and call python when necessary.



# make user enter only 1, 2, or 3. 
