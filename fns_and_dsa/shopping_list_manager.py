# Create an empty shopping list.
shopping_list = []

# Implement functionality to add items to the list, remove items, and display the current list.
"""
    Requirements:
Core Functionality:

Your script should start with an empty list named shopping_list. Done
Implement functionality to add items to the list, remove items, and display the current list. Done

User Interface:

Use a loop to continuously display a menu with options to the user until they choose to exit. The menu should offer options to add an item, remove an item, view the list, and exit.
For adding items, prompt the user for the item name and append it to shopping_list.
For removing items, ask the user for the item name and remove it from shopping_list. If the item is not found, display a message indicating so.
To view the list, print each item in shopping_list to the console.
Ensure your script handles invalid menu choices gracefully.
"""

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# To add to the list

def add_to_list(item):
    shopping_list.append(item)
    print(f'"{item}" has been added to the shopping list.')

# To remove from the list
def remove_from_list(item):
    try:
        shopping_list.remove(item)
        print(f'"{item}" has been removed from the shopping list.')
    except ValueError:
        print(f'"{item}" not found in the shopping list.')

# To view the list
def view_list():
    if shopping_list:
        print("Current shopping list:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is currently empty.")

def main():
    while True:
        display_menu()

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_to_list(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_from_list(item)
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting the shopping list application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()