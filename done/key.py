import random
import sys
from math import sqrt

def random_position():#x,y
    x = random.randint(0,5)
    y = random.randint(0,5)
    return [y, x]

def out_of_map():
    if player_position[0] > 5:
        print('wychodzisz poza mape, zawroc.')
        player_position[0] -= 1
 #y
    if player_position[0] < 0:
        print('wychodzisz poza mape, zawroc.')
        player_position[0] += 1


    if player_position[1] > 5:
        print('wychodzisz poza mape, zawroc.')
        player_position[1] -= 1
 #x
    if player_position[1] < 0:
        print('wychodzisz poza mape, zawroc.')
        player_position[1] += 1

moves_amount = 0
player_position = [0, 0]         #a 
key_position= random_position()          #b
distance_before_move = sqrt((key_position[0] - player_position[0]) ** 2 + (key_position[1] - player_position[1]) ** 2)

if player_position == key_position:
    player_position = random_position()

print('==================================================================')
print('szukasz klucza!  w - przod,  s - tyl,  a - lewo,  d - prawo  lub q - wyjscie')
print('jestes w:', player_position)
# print('key_position:', key_position)
print('======================')

while player_position != key_position:
    next_move = input('podaj ruch: ').lower()

    match next_move:
        case 'q':
            print('wychodze z gry :(')
            quit()
        case 'w':
            player_position[0] += 1
            out_of_map()
            moves_amount += 1
        case 's':
            player_position[0] -= 1
            out_of_map()
            moves_amount += 1
        case 'a':
            player_position[1] -= 1
            out_of_map()
            moves_amount += 1
        case 'd':
            player_position[1] += 1
            out_of_map()
            moves_amount += 1

    print()
    print('======================')
    print('jestes w:', player_position)
    # print(distance_before_move)
    print('======================')

    distance_after_move = sqrt((key_position[0] - player_position[0]) ** 2 + (key_position[1] - player_position[1]) ** 2)
    if distance_before_move > distance_after_move:
        print('cieplo')
    else:
        print('zimno')

    distance_before_move = distance_after_move
print(f'brawo znalazles klucz w {moves_amount} ruchach')
sys.exit()



