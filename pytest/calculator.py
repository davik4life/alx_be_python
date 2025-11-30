def addition( a, b):
    return a + b

def subtraction( a, b):
    return a - b

def multiplication( a, b):
    return a * b

def division( a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            print(f"Result: {addition(num1, num2)}")
        elif operation == '-':
            print(f"Result: {subtraction(num1, num2)}")
        elif operation == '*':
            print(f"Result: {multiplication(num1, num2)}")
        elif operation == '/':
            print(f"Result: {division(num1, num2)}")
        else:
            print("Invalid operation. Please choose from +, -, *, /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()