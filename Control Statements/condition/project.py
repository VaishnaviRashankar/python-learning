num1=float(input("Enter number1 = "))
num2=float(input("Enter number2 = "))
choice = input("Select your choice + - * /")
if choice == '+':
    print(f'Addition :{num1+num2}')
elif choice == '-':
    print(f'Substraction :{num1-num2}') 
elif choice == '*':
    print(f'Multiplication :{num1*num2}')
elif choice == '/':
    print(f'division :{num1/num2}')
elif choice == "**":
    print(f'Exponention:{num1**num2}')
else:
    print("Invalid Choice")