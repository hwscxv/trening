from random import randint

def main():
    weight = 0
    number_of_loads = 0


    while weight < 50:
        weight += int(input('podaj mase ladunku'))
        number_of_loads += 1

    print(f'zaladowano ciezarow lacznie {weight}, ilosc ladunkow {number_of_loads}, musisz doplacic za {weight-50}kg')

    while True:
        entered = input('podaj liczbe lub enter aby wyjsc')
        if entered == "":
            break
        
        number = int(entered)
        for n in range(1, number+1):
            if number % n == 0:
                print(n, end=' ') 

        print()


    def get_positive_number():
        number = int(input('pozytywna liczba '))
        if number > 0:
            return number
        else:
            return False
    
    while step := get_positive_number():  #przypisuje wynik z get_positive_number do step uzywajac := !
        print(f'liczba {step} jest OK')





    def throw():
        a = randint(1,6) 
        b = randint(1,6)
        if a == b:
            return True


    i_can_leave_prison = False
    no_of_tries = 0

    while not i_can_leave_prison:
        if throw():
            i_can_leave_prison = True
        no_of_tries += 1



    print(f'wyszedlem z wiezienia po {no_of_tries} probach')
main()
