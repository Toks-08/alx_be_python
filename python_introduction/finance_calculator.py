annual_interest_rate = 0.05
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
projected_saving1 = monthly_savings * 12
projected_saving1 += int(projected_saving1 * annual_interest_rate)
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year,with interest ${projected_saving1}")
