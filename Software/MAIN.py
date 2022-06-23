
from funcs import *
from data import *
clear()

while True:
    clear()
    print(f'---Main Menu---\n')
    x = show_menu(menu_main)
    if x not in list(menu_main.keys()):
        clear()
        continue

    if menu_main[x] == "Exit":
        clear()
        quit()

    if menu_main[x] == "Log":
        showlog()
        continue

    while menu_main[x] in list(menu_main.values()):
        clear()
        game = menu_main[x]
        print(f'---{game}---  ', end="", flush=True)
        print(eval(f'{game}.Desc') + "\n") #Yeah i just make command strings and eval them, you scared?

        y = show_menu(menu_game)
        if y not in list(menu_game.keys()):
            clear()
            continue

        if menu_game[y] == "Menu":
            break

        if menu_game[y] == "Ruleset":
            clear()     
            print(eval(f'{game}.{menu_game[y]}'))
            input("\nPress Enter to continue...")

        if menu_game[y] == "Play":
            totuser, totbank, totmatch, matched = [],[],[],0

            rollamtcheck = eval(f'len({game}.nchs_amt)')
            for rolls in range(rollamtcheck): #Just for EuroJ since you roll two indp sets in one game

                min = eval(f'{game}.roll_range[{rolls}]["min"]')
                max = eval(f'{game}.roll_range[{rolls}]["max"]')
                amt = eval(f'{game}.nchs_amt[{rolls}]')

                userticket  = let_user_choose(min, max, amt)
                bankticket  = let_bank_choose(min, max, amt)
                matched    += len(set(userticket) & set(bankticket))

                totuser.append(userticket)
                totbank.append(bankticket)
                totmatch.append(matched)

            csvwrite(game,totuser)
            csvwrite(game,totbank,'bank')
            csvwrite(game,totmatch,'match')

            clear()
            if matched>0:
                input(f'Congrats! You matched {matched} numbers total!!\n\nPress Enter to continue...')
            else:
                input(f'No Luck...\n\nPress Enter to continue...')
            break