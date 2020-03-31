"""
Napisz program, który na podstawie wprowadzonych wymiarów opakowania obliczy jego objętość oraz sprawdzi, czy jest ona większa od 1 litra (1000 cm3).
"""
wymiar_1 = int(input("Podaj wymiar 1 w cm: "))
wymiar_2 = int(input("Podaj wymiar 2 w cm: "))
wymiar_3 = int(input("Podaj wymiar 3 w cm: "))

objetosc = wymiar_1 * wymiar_2 * wymiar_3

print(f"Objetosc opakowania to: {objetosc} cm3")

print(f"Czy opakowanie ma objetosc wieksza niz 1 litr ? {objetosc > 1000}")