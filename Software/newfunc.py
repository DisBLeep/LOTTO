import random as r
import os
from sqlite3 import Row
import time
import csv
from menu_dicts import *



def clear():
    os.system('cls||clear')

def rand_array(min, max, amount):
    result = r.sample(range(min, max), amount)
    #if debug:
        #print(result)
    return result

def log(type, msg):
    logfile = open("logfile.txt", "a")
    logfile.write(f'{timestamp()}|{type}|{msg}\n')
    logfile.close()

def timestamp():
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%d.%m.%y|%H:%M:%S", named_tuple)
    return time_string

def askYN(ask):
    answers = ['Y','N']
    user_answer = ''
    while user_answer.upper() not in answers:
        user_answer = input(f'{ask} (Y/N)')
    return user_answer.upper()

def let_user_choose(min, max, amt):
    choice_pallet = list(range(min, max))
    choice_commit = []
    while len(choice_commit)<amt:
        clear()
        print(f'Choose from: {choice_pallet}')
        print(f'{len(choice_commit)}/{amt} Choosen: {choice_commit}')
        print('\n')
        choosen = input('Submit Number from the range above: ')
        try:
            choosen = int(choosen)
            if choosen in choice_pallet:
                choice_pallet.remove(choosen)
                choice_commit.append(choosen)
        finally:
            continue
    clear()
    commit_ticket = askYN(f'Commit Numbers:{choice_commit}?')
    if commit_ticket == 'Y':
        input('Submitted! Thank you!\n\nPress Any to continue..')
        return choice_commit
    else:
        exit


def show_menu(menu):
    options = list(menu.keys())
    menu_choice = ''
    while menu_choice not in options:
        #clear()
        for entry in options: 
            print(f'[{entry}] - {menu[entry]}')
        menu_choice = input(f'\nWybierz: {", ".join(options[:-1])} lub {options[-1]}\n>')
    return menu_choice

def csvwrite(Game, Numbers, Player='user'):
    header   = ['Time', 'Player', 'Game', 'Numbers']
    Time = timestamp()
    to_write = [Time, Player, Game, Numbers]
    with open('GameLog.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(to_write)

