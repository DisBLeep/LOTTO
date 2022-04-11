from cgi import print_arguments
import random
import os
import time
#from main import *

debug = True

def clear():
    os.system('cls||clear')

def rand_array(min, max, amount):
    result = random.sample(range(min, max), amount)
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
    answers = ['Y','N','EXIT']
    user_answer = ''
    while user_answer.upper() not in answers:
        user_answer = input(f'{ask} (Y/N/Exit)')
    return user_answer.upper()

def let_user_choose(min, max, amount_to_choose):
    choice_pallet = list(range(min, max))
    choice_commit = []
    while len(choice_commit)<amount_to_choose:
        clear()
        print(f'Choose from: {choice_pallet}')
        print(f'{len(choice_commit)}/{amount_to_choose} Choosen: {choice_commit}')
        print('\n')
        choosen = input('Submit Number from the range above: ')
        try:
            choosen = int(choosen)
            if choosen in choice_pallet:
                choice_pallet.remove(choosen)
                choice_commit.append(choosen)
        finally:
            continue
    YN = askYN(f'Commit Numbers:{choice_commit}?')
    if YN == 'Y':
        return choice_commit
    else:
        exit
