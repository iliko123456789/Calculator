while True:
    question = input("What calculation do you want (+, -, *, /)? Type 'stop' or 'off' to exit: ")
    
    if question.lower() in {'stop', 'off'}:
        break
    
    number = float(input("Enter the first number: "))
    number_2 = float(input("Enter the second number: "))
    
    if question == "/" and number_2 == 0 or number == 0:
        print("remember you cannot / 0 ok?")
    elif question == "/":
        print(number / number_2)
    elif question == "*":
        print(number * number_2)
    elif question == "-":
        print(number - number_2)
    elif question == "+":
        print(number + number_2)
    else:
        print("Invalid operation! Please enter a valid operation (+, -, *, /).")