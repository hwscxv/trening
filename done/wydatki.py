from pathlib import Path

expenses = []

expense_type = ['dom', 'rozrywka', 'jedzenie', 'inny']
month_value = {1:'styczen', 2:'luty', 3:'marzec', 4:'kwiecien', 5:'maj', 6:'czerwiec', 7:'lipiec', 8:'sierpien', 9:'wrzesien', 10:'pazdziernik', 11:'listipad', 12:'grudzien'}

# def save_to_file(month):

#     with open(f'./wydatki/expenses.txt', 'w', encoding='utf-8') as f:
#         f.write('\n'.join(f'{tup[0]}-{tup[1]}-{tup[2]}' for tup in expenses))

#     print('zapisano!')

def add_expenses(month):
        # while True:
        print()
        expense_amount = int(input('podaj kwote '))

        for index, type in enumerate(expense_type):
            print(f'{index}. {type}')
        print()
        
        expense_choice = int(input('wybierz kategorie '))
        # if expense_choice > len(expense_type):
        #     print('niepoprawny wybor kategorii')
        #     break

        expense = [expense_amount, expense_type[expense_choice], month]
        expenses.append(expense)
        
def show_expenses(month):  
    print()
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')

def add_expense_type():
    expense_type.append(input('podaj nowa kategorie '))

def show_stats(month):
    number_of_expenses_month = sum(1 for _, _, expense_month in expenses if expense_month == month)                         #month
    number_of_expenses_year = sum(1 for _, _, _ in expenses)                                                                         #year
    year_expenses = sum(expense_amount for expense_amount, _, _ in expenses)                                                         #year
    average_year_expenses  = year_expenses / number_of_expenses_year

    if number_of_expenses_month > 0:
        
        month_expenses = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)     #month
        average_month_expenses = month_expenses / number_of_expenses_month                                                  #month          
        
        print()
        print('Statystki wydatkow:')
        print()
        print('w miesiacu:')
        print()
        print('lacznie:',month_expenses, 'pln')
        print('sredni:', average_month_expenses)
        print('ilosc:', number_of_expenses_month)
    else:
        print()
        print('brak wydatkow do wyswietlenia w tym miesiacu')

    if len(expenses) < 0:
        print('brak wydatkow do wyswietlenia')    

    else:
        print()
        print('w roku:')
        print()
        print('lacznie', year_expenses, 'pln')
        print('sredni:', average_year_expenses)
        print('ilosc:', number_of_expenses_year)
        print()
        
        
# Path('./wydatki').mkdir(exist_ok=True)
# f = open('./wydatki/expenses.txt', "w")

while True:
    print()  
    month = int(input('wybierz miesiac 1-12 '))

    while True:
        print('----------------------------')
        print(month_value[month])
        print()
        print('0. powrot do wyboru miesiaca')
        print('1. wyswietl szczegoly wydatkow')
        print('2. dodaj wydatek')
        print('3. nowy typ wydatku')
        print('4. statystyki wydatkow')
        # print('5. zapisz do pliku')
        user_choice = int(input('wybierz opcje'))

        if user_choice == 0:
            break
        if user_choice == 1:
            show_expenses(month)
        if user_choice == 2:
            add_expenses(month)
        if user_choice == 3:
            add_expense_type()
            # print(expenses)
        if user_choice == 4:
            show_stats(month)
        if user_choice == 5:
            save_to_file(month)
            


