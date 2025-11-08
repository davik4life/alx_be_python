monthlyIncome = input("Enter your monthly income: ")
monthlyExpenses = input("Enter your monthly expenses: ")
interestRate = 0.05
year = 12
monthlySavings = int(monthlyIncome) - int(monthlyExpenses)
projectedSavings = int(monthlySavings * year + (monthlySavings * year * interestRate))
print(f"Your monthly savings are: ${monthlySavings}.")
print(f"Projected savings after one year, with interest, is: ${projectedSavings}.")