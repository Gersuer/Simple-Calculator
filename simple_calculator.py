#Receive from the user the math operations
#Desenvolver uma calculadora que permita realizar operações básicas, como adição, subtração, multiplicação e divisão.

while True:
    operator = input("Type the operation that you want to do: '+'/'-'/'*'/ '/'\n ")
    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("Please, type one of the basics math operations")
    else:
        n1 = float(input("Type the first number:\n"))
        n2 = float(input("Type the second number:\n"))
        if operator == '+':
            result = n1 + n2
            print(f'The sum result between {n1} and {n2} is {result}')
        if operator == '-':
            result = n1 - n2
            print(f'The subtract result between {n1} and {n2} is {result}')
        if operator == '*':
            result = n1 * n2
            print(f'The multiplication result between {n1} and {n2} is {result}')
        if operator == '/':
            result = n1 / n2
            print(f'The division result between {n1} and {n2} is {result}')
        while True:
            get_out = input("Do you want to exit? Y/N \n").lower()
            if get_out != 'y' and get_out != 'n':
                print('Plese type yes(Y) or No(N)')
            if get_out == 'y' or get_out =='n':
                break
    if get_out == 'y':
        print("Thanks for testing our simple calculator.")
        break
