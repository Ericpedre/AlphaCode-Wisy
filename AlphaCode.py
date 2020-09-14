import re
import os
import sys

def banner():
    print('                 ******************************************                    ')
    print('      *******************************************************************      ')
    print('*******************************              **********************************')
    print('**************************       ALPHA CODE       *****************************')
    print('*******************************              **********************************')
    print('      *******************************************************************      ')
    print('                 ******************WELCOME*****************                \n\n')

def clearScreen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    banner

def lasted(elem):
    return int(elem[7])

# find related areas
def relatedAreas(word, datain):
    areas = []
    a = []
    for line in datain:
        if word.lower() not in line[5].lower():
            areas.append(line[5])
    a = set(areas)
    areas = list(a)

    i = 0
    for area in areas:
        print('[' + str(i) + ']' + area)
        i += 1
    area_index = input('\nEnter the number of an industry in which these types of clients are located:')


    for area in areas:
        if int(areas.index(area)) == int(area_index):
            return area

banner()

Input = input('Describe, in one word, the type of person to whom marketing is directed: \nExample: developer\n>')

# Open files to read
data = []
with open('people.in', 'r') as file:
    data1 = file.read().split('\n')
    for i in data1:
        data.append(i.split('|'))

with open('Learn.txt', 'r') as learnfile:
    learn = learnfile.read()  
rows = learn.split('\n')

# converting str to list
set_learn = []
for row in rows:
    if row != '':
        fields = row.split('|')
        yWords = fields[1].split(' ')
        nWords = fields[2].split(' ')

        seld = []

        seld.append(int(fields[0]))
        seld.append(yWords)
        seld.append(nWords)

        set_learn.append(seld)


pre_out = []
for row in set_learn:
    if Input in row[1]:
        for word1 in row[1]:
            for row in data:
                if word1.lower() in row[3] or word1.lower() in row[5]:
                    pre_out.append(tuple(row))

# traditional search
for row in data:
    if row[3].lower().find(Input.lower()) > -1 or row[5].lower().find(Input.lower()) > -1:
        pre_out.append(tuple(row))

search = []

search.append(relatedAreas(Input, pre_out))

for row in data:
    if row[5].lower().find(search[0].lower()) > -1:
        pre_out.append(tuple(row))

out = list(set(pre_out))

for i in out:
    print(i)
print(len(out))

while len(out) < 100:
    search = []
    search.append(relatedAreas(Input, pre_out))

    for row in data:
        if row[5].lower().find(search[0].lower()) > -1:
            pre_out.append(tuple(row))
    out = list(set(pre_out))

    for i in out:
        print(i)
    print(len(out))

out.sort(key=lasted, reverse=True)

with open('people.out', 'w') as out_file:
    i = 0
    while i < 100:
        out_file.write(str(out[i][0]) + '\n')
        i += 1
print('Ids of 100 prospects saved in ./people.out')