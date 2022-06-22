import os
from turtle import xcor
from newfunc import *
from menu_dicts import *
clear()

"""
lotto
Wybierz 6 liczb z 49
multi multi
Wytypuj swoje liczby z zakresu od 1 do 80.
eurojackpot
Wybierz 5 liczb z 50 i 2 liczby z 12 
"""

while True:
    clear()
    x = show_menu(menu_main)
    if menu_main[x] == "Exit":
        clear()
        quit()

    while menu_main[x] != "Exit":
        clear()
        game = menu_main[x]
        print(f'--{game}--\n')
        y = show_menu(menu_game)

        if menu_game[y] == "Menu":
            break

        if menu_game[y] == "Opis":
            clear()     
            print(eval(f'{game}.{menu_game[y]}'))
            input("\nPress Any to continue...")

        if menu_game[y] == "Graj":
            let_user_choose(
                min = eval(f'{game}.roll_range["min"]'),
                max = eval(f'{game}.roll_range["max"]'),
                amt = eval(f'{game}.roll_count'))

        















"""
    if menu[menu_choice] == "Menu":
        show_menu(menu_main)
    if menu[menu_choice] == "Zasady":
        eval(print(f'{menu_main[menu_choice]}.sdesc'))
"""