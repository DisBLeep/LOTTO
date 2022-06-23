import os
from newfunc import *
from menu_dicts import *
clear()

while True:
    clear()
    x = show_menu(menu_main)
    if menu_main[x] == "Exit":
        clear()
        quit()

    while menu_main[x] != "Exit":
        clear()
        game = menu_main[x]
        print(f'---{game}---  >', end="", flush=True)
        print(eval(f'{game}.Opis') + "\n")

        y = show_menu(menu_game)

        if menu_game[y] == "Menu":
            break

        if menu_game[y] == "Zasady":
            clear()     
            print(eval(f'{game}.{menu_game[y]}'))
            input("\nPress Enter to continue...")

        if menu_game[y] == "Graj":
            totuser, totbank, totmatch, matched = [],[],[],0
            rollcheck = eval(f'len({game}.nchs_amt)')

            for rolls in range(0,rollcheck):

                min = eval(f'{game}.roll_range[{rolls}]["min"]')
                max = eval(f'{game}.roll_range[{rolls}]["max"]')
                amt = eval(f'{game}.nchs_amt[{rolls}]')

                userticket = let_user_choose(min, max, amt)
                bankticket = let_bank_choose(min, max, amt)
                matched += len(set(userticket) & set(bankticket))

                totuser.append(userticket)
                totbank.append(bankticket)
                totmatch.append(matched)

                csvwrite(game,totuser)
                csvwrite(game,totbank,'bank')
                csvwrite(game,totmatch,'match')


            clear()
            if matched>0:
                input(f'Congrats! You matched {matched} numbers!!\n\nPress Enter to continue...')
            else:
                input(f'No Luck...\n\nPress Enter to continue...')
            break


    















"""
    if menu[menu_choice] == "Menu":
        show_menu(menu_main)
    if menu[menu_choice] == "Zasady":
        eval(print(f'{menu_main[menu_choice]}.sdesc'))
"""