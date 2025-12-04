"""
Docstring for polymorphism
    Practice Exercises

Exercise 1: Single Inheritance Instruction:

Create a base class Shape with a method calculate_area().
Create a subclass Rectangle that inherits from Shape and overrides calculate_area() to calculate the area of a rectangle.

Exercise 2: Multiple Inheritance Instruction:

Create two parent classes Bird and Mammal with methods fly() and run(), respectively.
Create a subclass Bat that inherits from both Bird and Mammal and implements fly() and run() methods

Exercise 3: Polymorphism with Duck Typing Instruction:

Create classes Dog, Cat, and Bird, each with a method make_sound().
Implement different behaviors for make_sound() in each class.
Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically.
"""

# Exercise 1: Single Inheritance

class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
# Exercise 2: Multiple Inheritance

# class Bird:
#     def fly(self):
#         return "Flying"

# class Mammal:
#     def run(self):
#         return "Running"

# class Bat(Bird, Mammal):
#     def fly(self):
#         return super().fly()

#     def run(self):
#         return super().run()
    
# Exercise 3: Polymorphism with Duck Typing

class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Bird:
    def make_sound(self):
        return "Chirp!"

def let_them_speak(animals):
    for animal in animals:
        print(animal.make_sound())

# Demonstration of the classes and methods
if __name__ == "__main__":
    # Exercise 1 demonstration
    rectangle = Rectangle(5, 10)
    print(f"Area of rectangle: {rectangle.calculate_area()}")

    # Exercise 2 demonstration
    # bat = Bat()
    # print(bat.fly())
    # print(bat.run())

    # Exercise 3 demonstration
    dog = Dog()
    cat = Cat()
    bird = Bird()
    animals = [dog, cat, bird]
    let_them_speak(animals)
    
