monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
interest_rate = 0.05
year = 12
monthly_savings = float(monthly_income) - float(monthly_expenses)
projected_savings = monthly_savings * year + (monthly_savings * year * interest_rate)
print(f"Your monthly savings are: ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")