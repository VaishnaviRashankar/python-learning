try:
    num1 = int(input('enter number1'))
    num2 = int(input('enter number2'))
    try:
        result = num1/num2
        print(f'Result:{result}')
    except ZeroDivisionError:
        print('you cannot divide with zero')
except ValueError:
    print('You must provide a valid input')