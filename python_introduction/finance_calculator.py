# Finance calculator
monthlyIcome = int(input("Enter your monthly income:"))
monthlyExpenses = int(input("Enter your total monthly expenses:"))
monthlySavings = monthlyIcome - monthlyExpenses
print("Your monthly savings are", monthlySavings)
projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)
print("Projected savings after one year, with interest, is:", projectedSavings)
