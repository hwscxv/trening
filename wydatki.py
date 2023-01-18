expenses = []
expense_type = ['dom', 'rozrywka', 'jedzenie', 'inny']
month_value = {1:'styczen', 2:'luty', 3:'marzec', 4:'kwiecien', 5:'maj', 6:'czerwiec', 7:'lipiec', 8:'sierpien', 9:'wrzesien', 10:'pazdziernik', 11:'listipad', 12:'grudzien'}


def add_expenses(month):
    
        expense_amount = int(input('podaj kwote '))

        for index, type in enumerate(expense_type):
            print(f'{index}. {type}')
        
        expense_choice = int(input('wybierz kategorie '))

        expense = (expense_amount, expense_type[expense_choice], month)
        expenses.append(expense)
        
def show_expenses(month):
   
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')

def add_expense_type():
    expense_type.append(input('podaj nowa kategorie '))

def show_stats(month):
    # if expenses[month] > 0:
        print('Statystki wydatkow:')
        month_expenses = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
        number_of_expenses = sum(1 for _, _, expense_month in expenses if expense_month == month)
        all_expenses_amount = sum(expense_amount for expense_amount, _, _ in expenses)
        average_month_expenses = month_expenses / number_of_expenses

        print('wszystkie wydatki tego miesiaca:',month_expenses)
        print('sredni wydatek tego miesiaca', average_month_expenses)
        print('liczba wydatkow tego miesiaca', number_of_expenses)
        print('wszystkie wydatki w tym roku', all_expenses_amount)
    # else:
    #     print('brak wydatkow')


while True:
    month = int(input('wybierz miesiac 1-12 '))

    while True:
        print()
        print(month_value[month])
        print('0. powrot do wyboru miesiaca')
        print('1. wyswietl szczegoly wydatkow')
        print('2. dodaj wydatek')
        print('3. nowy typ wydatku')
        print('4. statystyki wydatkow')
        user_choice = int(input('wybierz opcje'))


        if user_choice == 0:
            break
        if user_choice == 1:
            show_expenses(month)
        if user_choice == 2:
            add_expenses(month)
        if user_choice == 3:
            add_expense_type()
        if user_choice == 4:
            show_stats(month)
            
        


