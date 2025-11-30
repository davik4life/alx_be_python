class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

def main():
    try:
        calc = Calculator()
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            print(f"Result: {calc.addition(num1, num2)}")
        elif operation == '-':
            print(f"Result: {calc.subtraction(num1, num2)}")
        elif operation == '*':
            print(f"Result: {calc.multiplication(num1, num2)}")
        elif operation == '/':
            print(f"Result: {calc.division(num1, num2)}")
        else:
            print("Invalid operation. Please choose from +, -, *, /.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()