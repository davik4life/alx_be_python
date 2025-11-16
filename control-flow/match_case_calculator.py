num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /):")
result = 0.0
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            result = 0
    case _:
        print("Error: Invalid operation.")
        result = 0
print("The result is:", result)