# Problem Set 2, hangman.py
# Name: Echo
# Collaborators:
# Time spent: 2 hrs

## algorithm: bisection search
# -----------------------------

## Take inputs from the user
start_salary = float(input("Enter the starting salary: "))

## declare some constants
total_cost = 1000000.0
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
epsilon = 100

## Initialize month counter and current saving variable
portion_saved_max = 10000
portion_saved_min = 0
portion_saved = (portion_saved_max + portion_saved_min)//2
step = 0
current_savings = 0

## loop until the difference between current savings and the down payment is less than epsilon
while abs(current_savings - (total_cost * portion_down_payment)) > epsilon:

    current_savings = 0
    annual_salary = start_salary

    for month in range(36):

        current_savings += annual_salary/12*portion_saved/10000\
         + current_savings*r/12

        ## break out if the saving is already enough (reduce calculation time)
        if (current_savings - (total_cost * portion_down_payment) > epsilon):
            break

        ## semi_annual salary raise
        if (month + 1) % 6 == 0:
            annual_salary = annual_salary*(1 + semi_annual_raise)

    if current_savings - (total_cost * portion_down_payment) > epsilon:
        # savings exceed, reduce percentage
        portion_saved_max = portion_saved

    ## after 36 month, current saving not enough
    elif current_savings - (total_cost * portion_down_payment) < -epsilon:

        ## If saving is 100% but still not enough
        ## if portion_saved >= 9999:
        if (portion_saved_max - portion_saved_min) // 2 == 0:
            print("It is not possible to pay the down payment in three years.")
            exit()

        else:
            # saving not enough increase percentage
            portion_saved_min = portion_saved

    ## update the savings portion and recalculate
    portion_saved = (portion_saved_max + portion_saved_min)//2
    step += 1

    print(current_savings, portion_saved, portion_saved_max, portion_saved_min)

## print the output
print("Best savings rate: ", portion_saved/10000)
print("Steps in bisection search", step)
print("current saving", current_savings)
