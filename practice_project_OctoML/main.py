''' Practice Project - SLOT MACHINE '''
# define global constants to limit the amounts the user can enter. constant values are all caps and do not change. 
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

''' --- HELPER FUNCTION TO COLLECT THE AMOUNT THE USER WANTS TO DEPOSIT FOR BETTING --- '''
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

# call the function so it will run when main() is run
#deposit()


''' --- HELPER FUNCTION TO COLLECT THE NUMBER OF LINES THE USER WANTS TO BET ON --- '''
# how many lines does the user want to bet on
def get_number_of_lines():
# get deposit user has entered

    # define a while loop that will run a check against an input amount and 
    while True:
        # prompt the user
        lines = input(f"How many lines would you like to bet on? (1 - {str(MAX_LINES)})? ")

        # if the entered string contains all digits and is a valid whole number, then convert it into an integer so it can be used mathematically
        # if not, prompt the user to enter the appropriate input
        if lines.isdigit():
            # convert the string to an int
            lines = int(lines)

            # make sure the user has entered a number between 1 and the maximum lines allowed. if so, don't re-prompt - you are done with this loop.
            # if not, prompt them to enter a number between 1 and the maximum lines allowed
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Your number needs to be between 1 and {str(MAX_LINES)}. ")

        # if the string entered is not all digits and a positive number, prompt for a correct input value
        else:
            print("Please enter a number.")

    # return the amount   
    return lines

# call the function so it will run when main() is run
#get_number_of_lines()


''' --- HELPER FUNCTION TO COLLECT HOW MUCH OF THE DEPOSIT THE USER WANTS TO BET --- '''
# get deposit user has entered
def get_bet():
    # declare amount var that will hold user input 
    amount = 0

    # define a while loop that will run a check against an input amount and 
    while True:
        # prompt the user
        amount = input("How much would you like to bet?: $")

        # if the entered string contains all digits and is a valid whole number, then convert it into an integer so it can be used mathematically
        # if not, prompt the user to enter the appropriate input
        if amount.isdigit():
            # convert the string to an int
            amount = int(amount)

            # make sure the user has entered a number higher than zero. if so, don't re-prompt - you are done with this loop.
            # if not, prompt them to enter a larger amount
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Your amount needs to be between ${MIN_BET} and ${MAX_BET}.")

        # if the string entered is not all digits and a positive number, prompt for a correct input value
        else:
            print("Please enter a number.")

    # return the amount   
    return amount

# call the function so it will run when main() is run
#deposit()



''' --- DEFINE THE MAIN PROGRAM --- '''
# set up main function for your program so you can re-run the game if the user wants to play again
def main():
    # calculate the bets and balances
    balance = deposit()
    lines = get_number_of_lines()

    # check to make sure the bet amount is not more than the available balance
    while True:
        bet = get_bet()
        total_bet = lines * bet
        #balance = balance - total_bet

        if total_bet > balance:
            print(f"You don't have enough money to cover this bet. Your balance is currently ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}.")
    #print(f"Your remaining balance is ${balance}")


# call the main() function to run everything
main()


