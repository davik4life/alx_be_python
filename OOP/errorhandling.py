"""
Practice Exercises
Exercise 1: Handling ZeroDivisionError

Instructions:

Write a program that takes two numbers as input from the user and divides the first number by the second number.
Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.

Exercise 2: File Handling with FileNotFoundError

Instructions:

Write a program that attempts to open and read data from a file specified by the user.
Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.

Exercise 3: Custom Exception

Instructions:

Create a custom exception class called ValueTooHighError that inherits from the Exception class.
Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.
"""

# Exercise 1: Handling ZeroDivisionError
class ZeroDivisionHandler:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def divide(self):
        try:
            result = self.num1 / self.num2
            return result
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    
# Example usage:
handler = ZeroDivisionHandler(10, 0)
handler = ZeroDivisionHandler(0, 50)
handler2 = ZeroDivisionHandler(10, 2)
print(handler.divide())
print(handler2.divide())

# Exercise 2: File Handling with FileNotFoundError
class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            return f"Error: The file '{self.filename}' was not found."
        
# Example usage:
file_handler = FileHandler("non_existent_file.txt")
print(file_handler.read_file())

# Exercise 3: Custom Exception
class ValueTooHighError(Exception):
    """Custom exception raised when the value is too high."""
    pass

class ValueChecker:
    def __init__(self, value):
        self.value = value

    def check_value(self):
        if self.value > 100:
            raise ValueTooHighError("Error: The value is too high! It must be 100 or less.")
        else:
            return "Value is acceptable."
        
# Example usage:
checker1 = ValueChecker(150)
checker2 = ValueChecker(80)

try:
    print(checker1.check_value())
except ValueTooHighError as e:
    print(e)

try:
    print(checker2.check_value())
except ValueTooHighError as e:
    print(e)