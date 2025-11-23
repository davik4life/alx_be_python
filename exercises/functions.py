"""
    Practice Exercises
Exercise 1: Write a function to greet the user by name.

Instructions:

Define a function called that takes one parameter, (name).
Inside the function, create a greeting message that includes the name passed as an argument.
Print the greeting message using the print function.


Exercise 2: Create a function to calculate the area of a rectangle.

Instructions:

Define a function that takes two parameters, length and width.
Inside the function, multiply the length and width to calculate the area.
Use the return statement to return the calculated area.


Exercise 3: Develop a function to check if a number is even or odd.

Instructions:

Define a function that takes one parameter, number.
Inside the function,check the remainder after dividing the number by 2 is equal to zero.
If the remainder is zero, the number is even. Print a message indicating the number is even.
If the remainder is not zero, the number is odd. Print a message indicating the number is odd.
"""
# Exercise 1
def greet_user(name):
    greet = print(f"Hello {name}, Welcome to my function call.")
    return greet

greet_user("Victor")

# Exercise 2
def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(5, 3)
print("The area of the rectangle is:", result)

# Exercise 3
def check_even_odd(num):
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")

check_even_odd(7)
check_even_odd(10)
check_even_odd(0)

