## cost_of_meal
## Compute tax and tips of meal
## tax_rate = 7.5%
## tip = 18% of the meal amount (without the tax)


##Program Output
## tax amount, tip amount, and the grand total for the meal including both the tax and the tip 

cost_of_meal = int(input("Enter the cost of meal the meal : "))
tax_amount = 7.5/cost_of_meal * 100
tips_amount = 18/cost_of_meal * 100
grand_total = tax_amount + tips_amount + cost_of_meal

print("N%.2f" %tax_amount)
print("N%.2f" %tips_amount)
print("N%.2f" %grand_total)