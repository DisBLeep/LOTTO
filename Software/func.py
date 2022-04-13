import random as r
import os
import time
#from main import *

debug = True

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
    clear()
    commit_ticket = askYN(f'Commit Numbers:{choice_commit}?')
    if commit_ticket == 'Y':
        return choice_commit
    else:
        exit

def roll(game):
    local_roll = []
    for num in range():
        pass
    return

def bankroll(game):
    npc_count   = r.randint(game.min_npc, game.max_npc)
    npc_pay     = npc_count * game.cost
    #game.bank   += npc_pay
    game.bank_plus(npc_pay)
    print(f'{npc_count} npcs paid, current bank: {game.bank}')

def show_menu(menu):
    options=menu.keys()
    for entry in options: 
      print(f'[{entry}] - {menu[entry]}')

def dontask(dict): #Dict to Str that looks like a Dict (formerly 'dtstllad()')
    string = str(dict)
    string = string.replace('{','{\n')
    string = string.replace('}','\n}')
    string = string.replace(', ',',\n')
    return string

#---- ----SAVE LOGIC

def save(key='',val='',filename='data.txt'):
    #---- Intercepting file corruption, restoring default save files
    try: 
        with open(filename, 'r+') as savestate:
            eval(savestate.read()) == 'dict'
    except Exception as reason:
        print(f'Error: {reason}\nRestoring default save')
        from menu_dicts import default_save
        with open(filename, 'w+') as savestate:
            savestate.write(dontask(default_save))
    finally:
        with open(filename, 'r') as savestate:
            save_dict = eval(savestate.read())
    #---- Overwriting 
    with open(filename, 'w') as savestate:
        if val != '':
            if val == 'del':
                del save_dict[key]
            else:
                save_dict[key] = val
        savestate.write(dontask(save_dict))
    return save_dict
