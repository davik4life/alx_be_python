monthlyIncome = input("Enter your monthly income: ")
monthlyExpenses = input("Enter your total monthly expenses: ")
interestRate = 0.05
year = 12
monthlySavings = float(monthlyIncome) - float(monthlyExpenses)
projectedSavings = monthlySavings * year + (monthlySavings * year * interestRate)
print(f"Your monthly savings are: ${int(monthlySavings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projectedSavings)}.")