menu_main = {
    '1':'Lotto',
    '2':'Multi',
    '3':'EuroJ',
    '4':'Exit',
    'L':'Log'
}

menu_game = {
    '1':'Play',
    '2':'Ruleset',
    '3':'Menu'  
}

class Game():
    def __init__(game, name, roll_range, nchs_amt, sdesc, ruleset):
        game.name       = name          # Name of the game, simple... actually unused?
        game.roll_range = roll_range    # Sets of range definitions
        game.nchs_amt   = nchs_amt      # Amount of N to choose
        game.Desc       = sdesc         # Short Description
        game.Ruleset    = ruleset       # Buncha rules, doesnt apply, just for show

Lotto = Game(   name        = 'Lotto', 
                roll_range  = [{'min':1, 'max':49}], 
                nchs_amt    = [6],
                sdesc       = "Roll ONCE: 6 numbers between 1-49",
                ruleset     = '''
+ W losowaniu bierze udział 49 kul.
+ W zakładach prostych typuje się 6 z 49 liczb, a w zakładach systemowych 7 do 12 liczb.
+ Wygrywasz za 3,4,5,6 trafień.
+ Można skreślić do 8 zakładów metodą blankietową.
+ Metodą chybił - trafił można skreślić do 10 zakładów na jednym kuponie.
+ Opłata za jeden zakład to 3 zł, przy czym 25% to dopłata na rozwój sportu.
+ Występują kumulacje na wygrane I stopnia.
+ Na wygrane przeznacza się co najmniej 51 % łącznej kwoty stawek wpłaconych za udział w grze.'''
                )


Multi = Game(   name        = 'Multi Multi', 
                roll_range  = [{'min':1, 'max':80}], 
                nchs_amt    = [10],
                sdesc       = "Roll ONCE: 10 numbers between 1-80",
                ruleset     = '''
+ W losowaniu bierze udział 80 kul, losuje się 20 z nich.
+ W zakładach wybiera się od 1 do 10 z 80 liczb.
+ Wygrane są zależne od ilości typowanych liczb, poniżej znajdziesz table wygranych.
+ Można skreślić do 3 zakładów na blankiecie lub metodą chybił - trafił.
+ Opłata za jeden zakład to 2,50 zł, a z opcją PLUS - 5 zł.
+ W Multi Multi są okresy promocyjne, podczas których dana ilość skreśleń ma większe wygrane o 50%.
+ Na wypłaty przeznacza się co najmniej 51 % łącznej kwoty stawek wpłaconych za udział w grze.'''
                )

EuroJ = Game(   name        = 'Euro Jackpot', 
                roll_range  = [{'min':1, 'max':50},{'min':1, 'max':12}], 
                nchs_amt    = [5,2],
                sdesc       = "Roll TWICE: 5 numbers between 1-50 AND 2 numbers betweem 1-13",
                ruleset     = '''
+ W losowaniu bierze udział 50 kul, z których typuje się 5. Dodatkowo Gracz wybiera 2 z 12 kul i skreśla na blankiecie.
+ Aby trafić Jackpota, czyli kumulację trzeba poprawnie wytypować 5 oraz 2 liczby (5 + 2).
+ Cena za zakład to 12,50 zł.
+ Występują kumulacje na wygrane I stopnia, minimalna to 10 mln euro, a maksymalna to 120 mln euro. W przypadku przekroczenia tej kwoty, automatycznie zwiększa się wypłata za drugi stopień (5 + 1).
+ Kupon Eurojackpot można zakupić w każdej kolekturze Lotto, lub zagrać online na gry.lotto.pl
+ Zamknięcie sprzedaży na losowanie Eurojackpot odbywa się o godzinie 19:00 we wtorek oraz piątek (unieważnienia do godziny 19:04:55).
+ Różnice kursowe PLN/EUR są dokładane do puli najwyższych wygranych w Polsce w danym losowaniu.
+ W Polsce obowiązują tylko polskie kupony, podobnie jak np. w Niemczech tylko niemieckie.
+ Główna wygrana jest wypłacana w euro, a na życzenie w złotówkach.
+ Niższe wygrane są wypłacane w złotówkach.
+ Nie można dokupić Super Szansy do kuponu Eurojackpot.
+ Losowanie przeprowadza, ustala zasady i nadzoruje organizator loterii "Veikkaus Oy" w Finlandii.'''
                )