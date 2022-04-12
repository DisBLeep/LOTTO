import os
import random

from func import *
from menu_dicts import *

os.system('cls||clear')
#lotto
""" 3 zł 
Wybierz 6 liczb z 49 """
#multi multi
""" 2,5 zł
Wytypuj swoje liczby z zakresu od 1 do 80. """
#eurojackpot
""" 12,5 zł
Wybierz 5 liczb z 50 i 2 liczby z 12 """

Session = True
whereami = ''

show_menu(menu_main)
menu_choice = input()

#print(menu_Lotto['1'])

x = 'menu_' + menu_main[menu_choice]
y = f'show_menu({x})'
exec(y)

