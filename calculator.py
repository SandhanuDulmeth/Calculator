def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

def select_op(choice):
    if choice == '+':
        return add, '+'
    elif choice == '-':
        return subtract, '-'
    elif choice == '*':
        return multiply, '*'
    elif choice == '/':
        return divide, '/'
    elif choice == '^':
        return power, '^'
    elif choice == '%':
        return remainder, '%'
    elif choice == '#':
        return -1, None
    elif choice == '$':
        return 0, None
    else:
        raise ValueError("Invalid Operation")

while True:
    print("Select operation.")
    print("1. Add      : + ")
    print("2. Subtract : - ")
    print("3. Multiply : * ")
    print("4. Divide   : / ")
    print("5. Power    : ^ ")
    print("6. Remainder: % ")
    print("7. Terminate: # ")
    print("8. Reset    : $ ")

    while True:
        try:
            choice = input("Enter choice (+, -, *, /, ^, %, #, $): ")
            operation, symbol = select_op(choice)
            if operation == -1:
                print("Done. Terminating.")
                exit()
            elif operation == 0:
                print("Resetting calculator.")
                break
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = operation(num1, num2)
                print(f"{num1} {symbol} {num2} = {result}")
                break
        except ValueError as e:
            print("Error:", e)
            print("Please enter a valid operation and numbers.")

