while True:
    print("Welcome to Mowille's Counter/Calculator.")
    print("What would you like to do today?")
    print('1. Count Words')
    print('2. Use the calculator')
    Choice = (input('Enter your option: '))
    if Choice == '1':
        Text = (input('Enter your text: '))
        User_text = Text
        User_text = len(Text.split())
        print('The word count of your text is: ' + str(User_text))
        Continue = input('Would you like to continue? [Yes, No]')
        if Continue == 'Yes':
            continue
        elif Continue == 'No':
            print('Thanks for using.')
            break
    elif Choice == "2":
        print('1. Addition')
        print('2. Subtraction')
        print('3. Division')
        print('4. Multiplication')
        print('5. Modulus')
    Operation = input('Enter your operation: ')
    num1 = int(input('Enter your first number: '))
    num2 = int(input('Enter your second number: '))

    if Operation == "1":
        print(num1, '+', num2, '=', (num1+num2))
    elif Operation == "2":
        print(num1, '-', num2, '=', (num1-num2))
    elif Operation == '3':
        print(num1, '/', num2, '=', (num1/num2))
    elif Operation == '4':
        print(num1, '*', num2, '=', (num1*num2))
    elif Operation == '5':
        print(num1, '%', num2, '=', (num1 % num2))
    Continue = input('Would you like to continue? [Yes, No]')
    if Continue == 'Yes':
        continue
    elif Continue == 'No':
        print('Thanks for using.')
        break
