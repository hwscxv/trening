import random
import sys


def random_position():#x,y
    x = random.randint(0,5)
    y = random.randint(0,5)
    return [x,y]

def out_of_map():
    if player_position[0] > 5:
        print('wychodzisz poza mape, zawroc.')
        player_position[0] -= 1
 #x
    if player_position[0] < 0:
        print('wychodzisz poza mape, zawroc.')
        player_position[0] += 1


    if player_position[1] > 5:
        print('wychodzisz poza mape, zawroc.')
        player_position[1] -= 1
 #y
    if player_position[1] < 0:
        print('wychodzisz poza mape, zawroc.')
        player_position[1] += 1


moves_amount = 0
player_position = random_position()
key_position= random_position()




if player_position == key_position:
    player_position = random_position()


print('==================================================================')
print('szukasz klucza!  w - przod,  s - tyl,  a - lewo,  d - prawo  lub q - wyjscie')
print('jestes w:', player_position)
# print('key_position:', key_position)
print('======================')


while player_position != key_position:
    next_move = input('podaj ruch: ').lower()

    if next_move == 'q':
        sys.exit(0)
    if next_move == '_':
        print('niewlasciwy ruch, sprobuj ponownie')
        continue
    if next_move == 'w':
        player_position[1] += 1
        out_of_map()
        moves_amount += 1
    if next_move == 's':
        player_position[1] -= 1
        out_of_map()
        moves_amount += 1
    if next_move == 'a':
        player_position[0] += 1
        out_of_map()
        moves_amount += 1
    if next_move == 'd':
        player_position[0] -= 1
        out_of_map()
        moves_amount += 1
    
    print('jestes w:', player_position)
    
    if player_position == key_position:
        print(f'brawo znalazles klucz w {moves_amount} ruchach')

    if player_position[0] == key_position[0] + 1:
        print('cieplo')
    elif player_position[0] == key_position[0] - 1:
        print('cieplo')
    elif player_position[1] == key_position[1] + 1:
        print('cieplo')
    elif player_position[1] == key_position[1] - 1:
        print('cieplo')



