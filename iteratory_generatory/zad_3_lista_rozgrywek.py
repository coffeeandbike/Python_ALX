"""
Zaimplementuj generator zwracający listę wszystkich możliwych rozgrywek
na podstawie dostarczonej listy graczy. Uwzględnij rewanże.
Przykładowe użycie:
for player_1, player_2 in tournament(['A', 'B', 'C']):
(a,b)
(a,c)
(b,a)
(b,c)
(c,a)
(c,b)
"""

def tourmanent(gracze):
    for gracz_1 in gracze:
        for gracz_2 in gracze:
            if gracz_1 != gracz_2:
                yield (gracz_1, gracz_2)


for zawodnik1, zawodnik2 in tourmanent(['janek', 'franek', 'jurek']):
    print(zawodnik1, zawodnik2)

print(list(tourmanent(['janek', 'franek', 'jurek'])))



