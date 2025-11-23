from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_datetime)


# Calculate a future date:

def calculate_future_date(number_of_days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    return future_date.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    display_current_datetime()
    print()
    days = int(input("Enter number of days to add: "))
    print()
    future_date = calculate_future_date(days)
    print(f"Date after {days} days will be: {future_date}")



    