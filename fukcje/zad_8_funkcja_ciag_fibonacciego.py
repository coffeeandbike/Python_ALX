import pytest

liczba = int(input("Podaj liczne: "))

#sposob rekurencyjny:

def fib(liczba: int) -> int:

    if liczba < 0:
        raise ValueError("N nie moze byc mniejsze od 0")

    if liczba == 0:
        return  0

    if liczba == 1:
        return 1

    if liczba > 1:
        return fib(liczba -1) + fib(liczba -2)


print(fib(liczba))

def test_wartosc_ujemna():
    with pytest.raises(ValueError):
        fib(-1)

def test_dobrych_Liczb():
    assert fib(0) == 1
    assert fib(5) == 5
    assert fib(7) == 13
