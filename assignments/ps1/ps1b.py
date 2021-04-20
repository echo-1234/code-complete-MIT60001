
## Take inputs from the user
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save,\
as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

## declare some constants
portion_down_payment = 0.25
r = 0.04

## Initialize month counter and current saving variable
current_savings = 0
month = 0

## loop until the current savings is more than the down payment
while current_savings < (total_cost * portion_down_payment):
    current_savings += annual_salary/12*portion_saved + current_savings*r/12
    month += 1
    if month % 6 == 0:
        annual_salary = annual_salary*(1 + semi_annual_raise)

## print the output
print("Number of months:", month)
