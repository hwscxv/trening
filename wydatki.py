expenses = []
expense_type = ['dom', 'rozrywka', 'jedzenie', 'inny']

while True:
    month = int(input('wybierz miesiac 1-12'))

    while True:

        print()
        print('0. powrot do wyboru miesiaca')
        print('1. wyswietl wszystkie wydatki')
        print('2. dodaj wydatek')
        print('3. nowy typ wydatku')
        print('4. statystyki wydatkow')
        user_choice = int(input('wybierz opcje'))


        if user_choice == 0:
            break
        if user_choice == 2:

            expense_amount = int(input('podaj kwote wydatku'))
            
            for index, type in enumerate(expense_type):
                print(f'{index}. {type}')
            
            expense_type = int(input('wybierz rodzaj wydatku'))
            

