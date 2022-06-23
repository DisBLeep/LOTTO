import random as r
import os
import time
import csv
from data import *

#---UTILITIES

def clear():
    os.system('cls||clear')

def timestamp():
    currenttime = time.localtime()
    timestring = time.strftime("%d.%m.%y|%H:%M:%S", currenttime)
    return timestring

def askYN(ask):
    answers = ['Y','N']
    user_answer = ''
    while user_answer.upper() not in answers:
        clear()
        user_answer = input(f'{ask} (Y/N)')
    return user_answer.upper()

def show_menu(menu):
    options = list(menu.keys())
    menu_choice = ''
    if menu_choice.upper() not in options:
        #clear()
        for entry in options: 
            print(f'[{entry}] - {menu[entry]}') #NOW youre thinkin with yo dic's
        menu_choice = input(f'\nChoose: {", ".join(options[:-1])} or {options[-1]}\n>')
    return menu_choice.upper()

#---ROLL LOGIC

def let_bank_choose(min, max, amt):
    result = r.sample(range(min, max), amt)
    result.sort()
    return result

def let_user_choose(min, max, amt):
    choice_pallet = list(range(min, max+1))
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
        input('Submitted! Thank you!\n\nPress Enter to continue..')
        choice_commit.sort()
        return choice_commit
    else:
        return 'denied'

#---SAVE LOGIC

def csvwrite(Game, Numbers, Player='User'):
    createlog()
    if len(Numbers)>0:
        filename = 'GameLog.csv'
        Time = timestamp()
        to_write = [Time, Player, Game, Numbers]
        with open(filename, 'a', encoding='UTF8', newline='') as a:
            writer = csv.writer(a)
            writer.writerow(to_write)

def showlog():
    createlog()
    filename = 'GameLog.csv'
    clear()
    with open(filename, 'r', encoding='UTF8', newline='') as r:
        nice_csv = csv.reader(r)
        for row in nice_csv:
            print('{:<20}  {:<6}  {:<8} {:<40}'.format(*row))

    z = input(f'\nPress Enter to continue... (or type "clear" to clear the log)')
    if z == 'clear':
        os.remove(filename)
        input('Log Cleared\n\nPress Enter to continue...')

def createlog():
    filename = 'GameLog.csv'
    if not os.path.exists(filename):
        header   = ['Time', 'Player', 'Game', 'Numbers']
        with open(filename, 'w', encoding='UTF8', newline='') as w:
            writer = csv.writer(w)
            writer.writerow(header)
