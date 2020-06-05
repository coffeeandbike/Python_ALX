

import string

import sys

with open('pan-tadeusz.txt', "r", encoding ='utf-8') as file:

    dict = dict()

    data = file.readlines()

    for line in data:

        line = line.strip()

        line = line.lower()

        line = line.translate(line.maketrans("", "", string.punctuation))

        words = line.split(" ")

        for word in words:

            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1

        if '' in dict:
            del dict['']

print(f'In this txt file is {len(dict)} unique words')
print()
for key in list(dict.keys()):
    print(f"{key} : {dict[key]}")
