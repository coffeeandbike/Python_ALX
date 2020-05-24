import sys

try:
    file_name = sys.argv[1]

    with open(file_name) as file:
        data = file.read()

        # print(list(enumerate(data.split('\n'))))

        for line_number, line in enumerate(data.split('\n'), start=1):
            print(f'{line_number}: {line}')


except FileNotFoundError:
    print(f'Nie znaleziono pliku {file_name}')
    exit(1)

except IndexError:
    print(f'usage: python zad_1.py file.txt')
    exit(1)