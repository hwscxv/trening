expenses = []
expense_type = ['dom', 'rozrywka', 'jedzenie', 'inny']
month_value = {1:'styczen', 2:'luty', 3:'marzec', 4:'kwiecien', 5:'maj', 6:'czerwiec', 7:'lipiec', 8:'sierpien', 9:'wrzesien', 10:'pazdziernik', 11:'listipad', 12:'grudzien'}


def add_expenses():
    
        expense_amount = int(input('podaj kwote wydatku '))

        for index, type in enumerate(expense_type):
            print(f'{index}.{type}')
        
        expense_choice = int(input('wybierz rodzaj wydatku '))

        expense = (expense_amount, expense_type[expense_choice], month)
        
def show_expenses():
    print()


while True:
    month = int(input('wybierz miesiac 1-12 '))

    while True:
        print()
        print(month_value[month])
        print('0. powrot do wyboru miesiaca')
        print('1. wyswietl wszystkie wydatki')
        print('2. dodaj wydatek')
        print('3. nowy typ wydatku')
        print('4. statystyki wydatkow')
        user_choice = int(input('wybierz opcje'))


        if user_choice == 0:
            break
        if user_choice == 2:
            add_expenses()


