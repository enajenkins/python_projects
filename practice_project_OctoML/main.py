''' Practice Project - SLOT MACHINE '''

# get deposit user has entered
def deposit():
    # declare amount var that will hold user input 
    amount = 0

    # define a while loop that will run a check against an input amount and 
    while True:
        # prompt the user
        amount = input("How much do you want to deposit?: $")

        # if the entered string contains all digits and is a valid whole number, then convert it into an integer so it can be used mathematically
        # if not, prompt the user to enter the appropriate input
        if amount.isdigit():
            # convert the string to an int
            amount = int(amount)

            # make sure the user has entered a number higher than zero. if so, don't re-prompt - you are done with this loop.
            # if not, prompt them to enter a larger amount
            if amount > 0:
                break
            else:
                print("Your amount needs to be greater than zero.")

        # if the string entered is not all digits and a positive number, prompt for a correct input value
        else:
            print("Please enter a number.")

    # return the amount   
    return amount

# call the function so it will run when the main.py file is fired
deposit()
