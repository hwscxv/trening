import random
import sys

user_points = 0
pc_points = 0


options = ['kamien', 'papier', 'nozyce']



while True:
    if user_points == 5:
        print(f'wygrana wynik: {user_points}:{pc_points}')
    elif pc_points == 5:
        print(f'przegrana wynik: {pc_points}:{user_points}')
        sys.exit(0)

    user_input = input('wybierz kamien, papier, nozyce lub q aby wyjsc ').lower()

    if user_input == 'q':
        break
    if user_input not in options:
        continue

    pc_choice = options[random.randint(0, 2)]
    print()
    print('komputer wybral ' + pc_choice + '.')

    match user_input:
        case 'nozyce':

            if pc_choice == 'papier':
                print('punkt dla uzytkownika')
                user_points += 1
            elif pc_choice == 'kamien':
                print('komputer wygral')
                pc_points += 1
            else:
                print('remis')

        case 'papier':

            if pc_choice == 'kamien':
                print('punkt dla uzytkownika')
                user_points += 1
            elif pc_choice == 'nozyce':
                print('komputer wygral')
                pc_points += 1
            else:
                print('remis')

        case 'kamien':

            if pc_choice == 'nozyce':
                print('punkt dla uzytkownika')
                user_points += 1
            elif pc_choice == 'papier':
                print('komputer wygral')
                pc_points += 1
            else:
                print('remis')

    print()
    print(f'komputer: {pc_points}')
    print(f'gracz: {user_points}')