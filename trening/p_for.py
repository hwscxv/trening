def main():
    book = {                #slownik
        'title': 'w pustyni',
        'author': 'henryk',
        'release date': 1911,
        'country': 'poland',
        'type': 'powiesc'
    }

    print('='*50)

    for key in book:
        print(f'{key} {book[key]}')         #iterowanie na slowniku  nr1

    

    for key, value in book.items():          #iterowanie na slowniku  nr1
        print(key, value)


    

    print('='*50)
    string = 'Subuj! kanal'

    for _ in string:
        if _ == '!':
            break                            #break powoduje przerwanie petli wiec else sie nie wykonuje
        print(_)
    else:
        print('przejscie petli')               #else w petli for wykonuje sie z kazdym przejsciem petli





    print('='*50)

    capitals = ['warszawa', 'berlin', 'paris']
    countries = ['polska', 'niemcy','francja']

    print()
    for index, city in enumerate(capitals, start=1):         #iterowanie + index od 1
        print(f'{index} {city}')


    print()
    for country, capital in zip(countries,capitals):        #iterowanie po dwoch listach na raz
        print(f'stolica panstwa {country} jest {capital}')


    print()
    for _ in range(0,11):
        print(_)


main()
