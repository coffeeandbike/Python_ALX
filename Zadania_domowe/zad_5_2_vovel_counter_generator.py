'''
Zaimplementuj generator zwracający jedynie samogłoski z zadanego ciągu znaków:
​
Przykładowe użycie:
for char in Vowels('ala ma kota a kot ma ale'):
'''


def VolelCounerGenerator(text_to_count: str):
    """
    Function for generating list of vowels from string
    :param text_to_count:
    :return:
    """
    VOWELS = ['e', 'y', 'u', 'i', 'o', 'a']

    vowels_list = []

    for char in text_to_count:
        if char in VOWELS:
            vowels_list.append(char)

    yield vowels_list




zlicz = VolelCounerGenerator("co to ma byc do cholery")

for char in zlicz:
    print(char)

print('=' * 60)

zlicz2 = VolelCounerGenerator("lorem impum lorem ipsum lorem impus")
for char in zlicz2:
    print(char)
