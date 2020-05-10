'''
Napisz funkcję obliczającą liczbę znaków w zadanym napisie pomiędzy zadanymi znakami.
Znaki, pomiędzy którymi ma odbywać się zliczanie, powinny być argumentami z wartościami domyślnymi - odpowiednio < i >.
Nawiasy mogą być zagnieżdżone i mogą wystąpić wiele razy.
Znaki pomiędzy zagnieżdżonymi nawiasami liczone są zgodnie z poziomem zagnieżdżenia.
Przykład użycia:
#>>> policz_znaki('ala ma <kota> a kot ma ale')
4
#>>> policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']')
18
#>>> policz_znaki('a <a<a<a>>>')
6
'''

# 1 stworzenie funcji o odpowiedniej nazwie i argumentach i wartosciach domyslnych

# 2 zmienna: ile_znakow, poziom , ustawione poczatkowo na zero

# 3 petla for gdzie przechodziny przez wszystkie znaki i:

    #- jesli napotkales znak start to zwieksz poziom o 1
    #- jesli napotkales znak end to zmniejsz poziom o 1
    #jesli poziom jest >0 to to ile_znakow dodaje ten poziom

# 4 zwracam ilosc znakow

#start = input('Podaj znak \'start\'')
#end = input('Podaj znak \'end\'')
#napis = input('Podaj znapis ze znakami \'start\' i \'end\'')

napis = ("ala [kota [a kot]] ma [ale]")

def policz_znaki(napis: str, start: str ='[', end: str =']') -> int:
    poziom = 0
    ile_znakow = 0
    for znak in napis:
        if znak == start:
            poziom += 1
        elif poziom > 0:
            ile_znakow += poziom
        elif znak == end:
            poziom -= 1
    return ile_znakow

print(policz_znaki(napis))


def test_przyklad_z_treci_zadania():
    assert policz_znaki ('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki ('ala [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki ('a <a<a<a>>>') == 6

#testy dla ustego napisu

def test_pusty_napis():
    assert policz_znaki("") == 0

#test gdy bak start/end
def test_brak_start_end():
    assert policz_znaki("ala ma kota") == 0









