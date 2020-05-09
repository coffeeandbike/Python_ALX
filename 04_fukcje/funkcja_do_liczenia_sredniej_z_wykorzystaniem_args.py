
#funkcja do liczenia sredniej z wykorzystaniem *args

#np srednia z 10, 20 ,30 -> 20

def licznik_sredniej(*args: float) -> float:
    # dorobic sprawdzanie czy args sa liczbami

    #for i in args:
    if len(args) == 0:
        print("Nie podales argumentow")
        return None

    srednia = sum(args) / len(args)
    print(srednia)

licznik_sredniej(10,20,30,50, 'dupa')

def test_bez_argumentow():
    assert licznik_sredniej() == None

def test_ze_stringiem():
    assert licznik_sredniej(10,20,30) == 20





