# Problem Set 2, hangman.py
# Name: Echo
# Collaborators:
# Time spent: 2 hrs

## algorithm: bisection search
## use function
# -----------------------------


def calc_savings(current_savings, annual_salary, portion_saved,\
 total_down_payment, epsilon):
 '''
 Calculate the saving based on the salary and the saving portion_saved
 '''

    semi_annual_raise = 0.07
    r = 0.04

    for month in range(36):
        current_savings += annual_salary/12*portion_saved/10000\
         + current_savings*r/12
        if (current_savings - (total_down_payment) > epsilon):
            return (current_savings, portion_saved)
        if (month + 1) % 6 == 0:
            annual_salary = annual_salary*(1 + semi_annual_raise)

    return (current_savings, portion_saved)

## Take inputs from the user
annual_salary = float(input("Enter the starting salary: "))

## declare some constants
total_cost = 1000000.0
portion_down_payment = 0.25
epsilon = 100

## Initialize month counter and current saving variable
portion_saved_max = 10000
portion_saved_min = 0
portion_saved = (portion_saved_max + portion_saved_min)//2
step = 0
current_savings = 0

## loop until the difference between current savings and the down payment within epsilon
while abs(current_savings - (total_cost * portion_down_payment)) > epsilon:

    ## calculate the saving
    (current_savings, portion_saved) = calc_savings(0, annual_salary,\
     portion_saved, total_cost * portion_down_payment, epsilon)

    if current_savings - (total_cost * portion_down_payment) > epsilon:
        # saving exceed, reduce percentage
        portion_saved_max = portion_saved

    elif current_savings - (total_cost * portion_down_payment) < -epsilon:

        # after 36 month, current saving not enough
        if portion_saved >= 9999:
            # this condition may have problem?
            print("It is not possible to pay the down payment in three years.")
            exit()
        else:
            # saving not enough, increase percentage
            portion_saved_min = portion_saved

    # update the saving portion and loop
    portion_saved = (portion_saved_max + portion_saved_min)//2
    step += 1

    print(current_savings, portion_saved, portion_saved_max, portion_saved_min)

## print the output
print("Best savings rate: ", portion_saved/10000)
print("Steps in bisection search", step)
print("current saving", current_savings)
