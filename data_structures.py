"""
    Practice Exercise
Exercise 1: Create a list to store names of your favorite fruits. Write code to access the second element and print it.
Exercise 2: Define a dictionary to store information about your favorite book, including title, author, and genre. Use the method to retrieve the genre.
Exercise 3: Write a program to generate a random set of numbers between 1 and ten. Use set operations to remove duplicates and display the unique numbers.
"""


# Exercise 1
fav_fruits = ["Bananas", "Watermelon", "Guava", "Pineapples", "Coconuts"]

def print_second_fruit(fruits):
    second_fruit = fruits[1]
    print_it = print("The second fruit in the list is:", second_fruit)
    return print_it

print_second_fruit(fav_fruits)

# Exercise 2
fav_book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "genre": "Adventure Fiction"
}

fav_book_genre = fav_book.get("genre")
print("The genre of my favorite book is:", fav_book_genre)

# Exercise 3
import random
random_numbers = [random.randint(1, 10) for _ in range(10)]
unique_numbers = set(random_numbers)
print("The unique random numbers between 1 and 10 are:", unique_numbers)