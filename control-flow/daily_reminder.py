task = input("Enter your task:")
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = str(input("Is it time-bound? (yes/no): ")).lower()
print()

match (priority):
    case ("high"):
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is not time-bound, but should still be prioritized.")
    case ("medium"):
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is not time-bound. Schedule it accordingly.")
    case ("low"):
        if time_bound == "yes":
            print(f"Reminder: '{task}' is time-bound that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is not time-bound. It can be done at your convenience.")
    case _:
        print("Invalid input for priority or time-bound status.")