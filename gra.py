import sys



no_of_tries  = 5
word = 'sowa'
used_letters = []
user_word = []


def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter_in_word == letter:
            indexes.append(index)
    return indexes



for _ in word:
    user_word.append('_')
print("gra wisielec, odgadnij haslo ")



while True:
    
    print(user_word)
    letter = input('podaj litere ')
    found_indexes = find_indexes(word, letter)
    
    if len(found_indexes) == 0:
        print('nieprawidlowa litera, utrata zycia.')
        no_of_tries -= 1
        if no_of_tries == 0:
            print('utrata wszystkich zyc, koniec gry')
            sys.exit(0)

    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print('brawo wygrana')
            sys.exit(0)
        