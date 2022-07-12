def collatz(number):
    global numbers
    numbers.append(number)
    if number == 1:
        return 1
    elif number % 2 == 0:
        collatz(number//2)
    else :
        collatz(3*number+1)

numbers = []
try:
    n=int(input('輸入一個正整數:'))
    collatz(n)
    print(len(numbers))
except TypeError:
        print('輸入一個整數!')
except ZeroDivisionError:
    print('不能為0!')     
