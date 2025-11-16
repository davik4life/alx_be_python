task = input("Enter your task:")
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = str(input("Is it time-bound? (yes/no): ")).lower()
print()

match (priority, time_bound):
    case ("high", "yes"):
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case ("high", "no"):
        print(f"Reminder: '{task}' is not time-bound, but should still be prioritized.")
    case ("medium", "yes"):
        print(f"Reminder: '{task}' is time-bound. Try to complete it soon.")
    case ("medium", "no"):
        print(f"Reminder: '{task}' is not time-bound. Schedule it accordingly.")
    case ("low", "yes"):
        print(f"Reminder: '{task}' is time-bound. Don't forget to get to it.")
    case ("low", "no"):
        print(f"Reminder: '{task}' is not time-bound. It can be done at your convenience.")
    case _:
        print("Invalid input for priority or time-bound status.")

