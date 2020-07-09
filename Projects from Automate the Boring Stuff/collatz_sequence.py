def collatz(number) :
    if number % 2 == 0 :
        print(number // 2)
        return number // 2
    elif number % 2 != 0 :
        print(3 * number + 1)
        return 3 * number + 1

try :
    num = int(input('Give me a number: '))
except ValueError :
    print('Invalid : Please Input an Integer')
    num = int(input('Give me a number: '))
    
while num != 1 :
    num = collatz(num)
    

