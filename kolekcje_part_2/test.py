exampleSet = [{'type': 'type1'}, {'type': 'type2'}, {'type': 'type2'}, {'type': 'type3', 'title':'title'}]

keyValList = ['type2','type3']

new_list = list(filter(lambda d: d['type'] in keyValList, exampleSet))

print(new_list)



notice1 = {'kategoria': 1, 'tytul': 'Rower', 'opis': 'Bardzo dobry rower', 'cena': 2000.0, 'sprzedajacy': 'Jan Nowak',
     'telefon': '111 222 333', 'adres': 'Pcim Sredni'}

notice2 = {'kategoria': 2, 'tytul': 'dupa', 'opis': 'gruba dupa', 'cena': 1000.0, 'sprzedajacy': 'Jan Starak',
     'telefon': '123 456 789', 'adres': 'Wroclaw'}

board = []

board.append(notice1)
board.append(notice2)

print(board)

key_filter = 'tytul'
definition_filter = 'dupa'
new_board = []


for notice in board:
        new_board = list(filter(lambda element: element[key_filter] in definition_filter, board))

print(new_board)






