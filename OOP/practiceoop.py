"""
Practice Exercises
Exercise 1: Creating a Student Class

Instructions:

Define a Student class with attributes like name and age. Include a method to display student information.

Exercise 2: Creating a Product Catalog

Instruction:

Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock."""

# Exercise 1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_student_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

student1 = Student("Alice", 20)
student2 = Student("Victor", 36)
student1.display_student_info()
student2.display_student_info()

# Exercise 2
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.price * self.quantity
    

Product1 = Product("Laptop", 800, 15)
print()
Product2 = Product("Phones",450, 12)

print(f"The total value of {Product1.name} in stock is: ${Product1.total_value()}.")
print(f"The total value of {Product2.name} in stock is: ${Product2.total_value()}.")
