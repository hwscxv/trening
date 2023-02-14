import sys


answer = 'sowa'
no_of_tries = 5
user_word = []








print('gra zgadnij litere')

def find_indexes(letter, answer):
    indexes = []
    for index, letter_in_word in enumerate(answer):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes
    


for _ in answer:
    user_word.append('_')

while True:


    print(user_word)
    letter = input('podaj litere')
    found_indexes = find_indexes(letter, answer)

    if len(found_indexes) == 0:
        print('bledna litera utrata zycia')
        no_of_tries -= 1

        if no_of_tries == 0:
            print('utrata wszystkich zyc, przegrana')
            sys.exit(0)
    
    else:
        for index in found_indexes:
            user_word[index] = letter


        if "".join(user_word) == answer:
            print('brawo wygrales')
            sys.exit(0)


