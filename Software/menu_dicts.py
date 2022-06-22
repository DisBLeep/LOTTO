menu_main = {
    '1':'Lotto',
    '2':'Multi',
    '3':'EuroJ',
    '4':'Exit'
}

menu_game = {
    '1':'Graj',
    '2':'Zasady',
    '3':'Menu'  
}

class Game():
    def __init__(game, name, roll_range, roll_count, sdesc, zasady):
        game.name       = name
        game.roll_range = roll_range
        game.roll_count = roll_count
        game.Opis       = sdesc
        game.Zasady     = zasady

Lotto = Game(   name        = 'Lotto', 
                roll_range  = {'min':1, 'max':49}, 
                roll_count  = 6,
                sdesc       = "Gra popularna ze względu na swoją wszechstronność. Możesz używać wielokrotnych stawek i typować dowolną ilość liczb.",
                zasady      = '''
+ W losowaniu bierze udział 49 kul.
+ W zakładach prostych typuje się 6 z 49 liczb, a w zakładach systemowych 7 do 12 liczb.
+ Wygrywasz za 3,4,5,6 trafień.
+ Można skreślić do 8 zakładów metodą blankietową.
+ Metodą chybił - trafił można skreślić do 10 zakładów na jednym kuponie.
+ Opłata za jeden zakład to 3 zł, przy czym 25% to dopłata na rozwój sportu.
+ Występują kumulacje na wygrane I stopnia.
+ Na wygrane przeznacza się co najmniej 51 % łącznej kwoty stawek wpłaconych za udział w grze.'''
                )


Multi = Game(   name        = 'Lotto', 
                roll_range  = {'min':1, 'max':80}, 
                roll_count  = 10,
                sdesc       = "Najpopularniejsza gra Totalizatora Sportowego, oferuje bardzo wysokie wygrane w przypadku trafienia 6/6 liczb. Jednocześnie jest to najstarsza z gier losowych w Polsce.",
                zasady      = '''
+ W losowaniu bierze udział 80 kul, losuje się 20 z nich.
+ W zakładach wybiera się od 1 do 10 z 80 liczb.
+ Wygrane są zależne od ilości typowanych liczb, poniżej znajdziesz table wygranych.
+ Można skreślić do 3 zakładów na blankiecie lub metodą chybił - trafił.
+ Opłata za jeden zakład to 2,50 zł, a z opcją PLUS - 5 zł.
+ W Multi Multi są okresy promocyjne, podczas których dana ilość skreśleń ma większe wygrane o 50%.
+ Na wypłaty przeznacza się co najmniej 51 % łącznej kwoty stawek wpłaconych za udział w grze.'''
                )

EuroJ = Game(   name        = 'EuroJ', 
                roll_range  = {'min':1, 'max':50}, 
                roll_count  = 5,
                sdesc       = "Szansa na główną wygraną Eurojackpot to jak 1 do 139 838 159, w grze zastosowano aż 50 kul w jednym bębnie maszyny losującej oraz 12 w drugim.",
                zasady      = '''
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