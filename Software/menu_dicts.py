default_save = {
    'npc1':100,
    'npc2':200
}

menu_main = {
    '1':'Lotto',
    '2':'Multi Multi',
    '3':'Euro Jackpot',
    '4':'Exit'
}

menu_game = {
    '1':'Play',
    '2':'Help',
    '3':'Exit'  
}

class Game():
    def __init__(game, name, max_npc, cost, roll_range, roll_count, bank_min, bank):
        game.name       = name
        game.max_npc    = max_npc
        game.min_npc    = round(max_npc/100)
        game.cost       = cost
        game.roll_range = roll_range
        game.roll_count = roll_count
        game.bank_min   = bank_min
        game.bank       = bank
        game.bank_rolled= []

    def bank_plus(game, amount):
        if  game.bank < game.bank_min:
            game.bank = game.bank_min
        game.bank += amount
        return


Lotto = Game(   name        = 'Lotto', 
                max_npc     = 1000, 
                cost        = 3, 
                roll_range   = {'min':1, 'max':49}, 
                roll_count   = 6,
                bank_min    = 1000000,
                bank        = 0
                )
