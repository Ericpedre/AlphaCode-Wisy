import re
import sys
import os

def banner():
    print('                 ******************************************                    ')
    print('      *******************************************************************      ')
    print('*******************************              **********************************')
    print('**************************       ALPHA CODE       *****************************')
    print('*******************************  (TRAINING)  **********************************')
    print('      *******************************************************************      ')
    print('                 ******************WELCOME*****************                \n\n')

def clearScreen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    banner()

def findRowWithWord(words, data):
    rows = []
    a = []
    for word in words:
        for row in data:
            if row[3].lower().find(word.lower()) > -1 or row[5].lower().find(word.lower()) > -1:
                rows.append(tuple(row))
    a = set(rows)
    return list(a)

def relatedAreas(word, datain):
    areas = []
    a = []
    for line in datain:
        if line[5].lower().find(word.lower()) == -1:
            areas.append(line[5])
    a = set(areas)
    areas = list(a)

    i = 0
    for area in areas:
        print('[' + str(i) + ']' + area)
        i += 1
    area_index = input('Select a related industry number: ')


    for area in areas:
        if int(areas.index(area)) == int(area_index):
            return area
    
def wordsOnCurrentRolres():
    #### Comon words on CurrentRoles

    currentRoles = []
    a = []
    for line in pre_out:
        currentRoles.append(line[3])
    a = set(currentRoles)
    currentRoles = list(a)

    # separate words

    for sentence in currentRoles:
        sentence_split = re.split(',|:| |-|,',str(sentence))
        for word in sentence_split:
            words.append(word)

    # delete emptyWords

    with open('emptyWords.txt', 'r') as ew:
        ewwords = ew.read().split('\n')
        for item in ewwords:
            # for word in words:
            while item in words:
                words.remove(item)

    # count words
    ant = []
    for word in words:
        if word in ant:
            continue
        else:
            out_words.append([word, words.count(word)])
            ant.append(word)


search = [input('Describe, in one word, the type of person to whom marketing can be directed: \nExample: developer\n>')]
banner()
# set data
data = []
with open('people.in', 'r') as file:
    data1 = file.read().split('\n')
    for i in data1:
        data.append(i.split('|'))

pre_out = findRowWithWord(search, data)
#### Search words in areas
print(pre_out)
search.append(relatedAreas(search[0], pre_out))
pre_out = findRowWithWord(search, data)

words = []
out_words = []
wordsOnCurrentRolres()

###### Learn ######
with open('Learn.txt', 'r') as learnfile:
    learn = learnfile.read()  
rows = learn.split('\n')

set_learn = []

# Convert learn file in lists

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


# search for the word entered in the data
wordExist = None
yWords = []
nWords = []
index = []
for row in set_learn:
    if search[0] in row[1] or search[0] in row[2]:
        wordExist = True
        yWords = row[1]
        nWords = row[2]
        for word in out_words:
            if (word[0] in row[1]) or (word[0] in row[2]):
                index = row[0]
            else:
                clearScreen()
                answer = input('The word "' + search[0] + '" is directly related to ...\n' + word[0] + '\t[y/n]:')
                if answer == 'y':
                    yWords.append(word[0])
                elif answer == 'n':
                    nWords.append(word[0])
    else:
        wordExist = False


if wordExist:
    # write data to the list
    set_learn.pop(index)
    set_learn.insert(index, [index, yWords, nWords])
else:
    # search for the word entered in the data
    yWords = []
    nWords = []
    yWords.append(search[0])
    for word in out_words:
        clearScreen()
        answer = input('The word "' + search[0] + '" is directly related to ...\n' + word[0] + '\t[y/n]:')
        if answer == 'y':
            yWords.append(word[0])
        elif answer == 'n':
            nWords.append(word[0])
    set_learn.append([len(set_learn), yWords, nWords])

# the learned data is converted to str
datawrite = ''
saltoln = ''
for row in set_learn:
    yWords = ''
    nWords = ''
    space = ''
    for word in row[1]:
        yWords = yWords + space + word
        space = ' '
    space = ''
    for word in row[2]:
        nWords = nWords + space + word
        space = ' '
    
    fields = str(row[0]) + '|' + yWords + '|' + nWords

    datawrite = datawrite + saltoln + fields
    saltoln = '\n'
datawrite

# the learned data is writed in file
with open('Learn.txt', 'w') as learnfile:
    learnfile.write(datawrite)