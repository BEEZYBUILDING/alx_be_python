#week 4 project
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))



# Ask for operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using match-case
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation. Please choose from +, -, *, /.")


                
