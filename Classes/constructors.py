"""
    Practice Exercises
Exercise 1: Constructors and Destructors Instructions:

Create a Person class with attributes like name and age. Implement a constructor (__init__) to initialize these attributes.
Also, implement a destructor (__del__) method to print a farewell message when an object is deleted.

Exercise 2: Magic Methods (str and repr) Instructions:

Create a Book class with attributes like title, author, and pages.
Implement both __str__ and __repr__ magic methods to provide different string representations of the book object.

Exercise 3: Class Inheritance Instructions:

Create a base class Animal with methods like eat and sleep.
Create a subclass Dog that inherits from Animal and adds a method bark.
Create instances of both classes and demonstrate method inheritance.

"""
# Exercise 1: Constructors and Destructors
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Hello, {self.name}! You are {self.age} years old.")

    def __del__(self):
        print(f"Farewell, {self.name}!")

# Exercise 2: Magic Methods (str and repr)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
    
# Exercise 3: Class Inheritance
class Animal:
    def eat(self):
        return "The animal is eating."

    def sleep(self):
        return "The animal is sleeping."
    
class Dog(Animal):
    def bark(self):
        return "Bark!"
# Demonstration of the classes and methods
if __name__ == "__main__":
    # Exercise 1 demonstration
    person = Person("Alice", 30)
    del person  # Triggering destructor

    # Exercise 2 demonstration
    book = Book("1984", "George Orwell", 328)
    print(str(book))   # Using __str__
    print(repr(book))  # Using __repr__

    # Exercise 3 demonstration
    animal = Animal()
    dog = Dog()
    print(animal.eat())
    print(animal.sleep())
    print(dog.eat())  # Inherited method
    print(dog.sleep())  # Inherited method
    print(dog.bark())  # Dog's own method

    