import random
import sys  
import string
password = []

characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left

        #ile pozostalo          ile ma byc
    if characters_left < 0 or number_of_characters > characters_left:
        print('liczba spoza przedzialu 0', characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print('pozostalo znakow', characters_left)






print('generator hasel')
p_len = int(input('podaj dlugosc generowanego hasla'))

if p_len < 5:
    print('haslo musi miec minumum 5 znakow')
    sys.exit(0)
else:  
    characters_left = p_len



low =     int(input('podaj ilosc malych liter'))
update_characters_left(low)
high =    int(input('podaj ilosc duzych liter'))
update_characters_left(high)
special = int(input('podaj ilosc specialnych znakow'))
update_characters_left(special)
digits =  int(input('podaj ilosc cyfr'))
update_characters_left(digits)



if characters_left > 0:
    print('nie wszystkie znaki zostaly wykorzystane, zostana dodane male litery')
    low += characters_left


for _ in range(p_len):
    if low > 0:
        password.append(random.choice(string.ascii_lowercase))
        low -= 1
    if high > 0:
        password.append(random.choice(string.ascii_uppercase))
        high -= 1
    if special > 0:
        password.append(random.choice(string.punctuation))
        special -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1


random.shuffle(password)
print('twoje haslo to:' , "".join(password))
        


