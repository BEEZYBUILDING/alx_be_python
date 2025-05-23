#This is the fifth python project.
income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expenses: "))

monthly_savings = income - expense

annual_savings = savings * 12 + (savings * 12 * 0.05)

print("Your monthly savings are", monthly_savings)
print("Projected savings after one year, with interest, is:", annual_savings)
