''' Practice Project - SLOT MACHINE (super simple) '''

# import random to generate gambling results
''' NOTE: random is not part of the math module in Python
    random.randint(a, b): Returns a random integer between a and b (inclusive).
    random.choice(sequence): Returns a random element from a non-empty sequence (like a list).
    random.random(): Returns a random float between 0.0 and 1.0.
'''
import random

# define global constants to limit the amounts the user can enter. constant values are all caps and do not change. 
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# define global constants to simulate the revolving reels 
ROWS = 3
COLUMNS = 3

# define a global dictionary to define how many of each symbol is on a reel
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8    
}

# define a global dictionary to define each symbol's multiplier
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2    
}


''' --- HELPER FUNCTION TO CHECK THE SLOT LINES FOR MATCHES AND RETURN WINNINGS --- '''
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    # look through each of the the slot result rows for a win
    for line in range(lines):
        # check to see if all symbols in the current line are the same:
        # get the symbol that is in the first column of the row
        symbol = columns[0][line]
        # loop through the columns to compare the first symbol to each one in the line
        for column in columns:
            # the symbol to check = column at the current row we are looking at
            symbol_to_check = column[line]
            # if there is a mismatch, exit this loop and go back to the previous loop to check the next line
            # if you reach the end of the loop without breaking, the symbols are the same and the won.
            if symbol != symbol_to_check:
                break
        else: # else statement with for loop that will run if break is executed
            winnings += values[symbol] * bet
            winning_lines.appemd(lines + 1)

    return winnings, winning_lines


''' --- HELPER FUNCTION TO GENERATE A RANDOM SLOT MACHINE RESULT --- '''
# pass in the reel values needed
def get_slot_machine_spin(rows, cols, symbols):
    # randomly pick values for the columns by creating a list of all possible values and randomly picking a value from the list
    all_symbols = []
    # loop through the dictionary and add the symbols to the list
    # symbols.items() gives you both the key and the value from the dictionary. 
    # This prevents you from having to reference the values manually while looping through the keys
    for symbol, symbol_count in symbols.items():

        # add symbols to list using another for loop and an anonymous var (_). 
        # _ prevents an unused var error when the count doesn't matter (if var is greyed out and loop still works, you can use _)
        # NOTE: if the loop above produces: symbol = A and symbol_count = 2, 
        # then this second loop will run 2 times and add two A symbols to the all_symbols list
        for _ in range(symbol_count): 
            # add the symbol to the list
            all_symbols.append(symbol)

    # create a columns list that will contain the randomized lists of symbols for each slot column
    # this will eventually result in a nested list: columns = [[], [], []]
    columns = []     

    # generate a number of columns based on the number you specified in the args. 
    # for every column, generate the values inside the columns (a certain number of symbols) based on the number of rows you have
    for _ in range(cols):
        column = []
        # NOTE: if there are only 2 of the symbol A available, it should not be added more than twice
        # create a copy of the all_symbols list to work with during the loop 
        current_symbols = all_symbols[:]

        # loop through the number of values that you need to generate which is equal to the number of rows you need to generate.
        for _ in range(rows):
            # pick randoom values for each row in the column. 
            value = random.choice(current_symbols) 
            # remove the value you just added from the working list so you dont pick it again
            current_symbols.remove(value)
            # add that value to the column list
            column.append(value)

        # add column you just created to the slot columns list
        columns.append(column)

    # return the columns nested list (where every interior list gives you the symbol values for each column).
    return columns


''' --- HELPER FUNCTION TO PRINT OUT THE SLOTS--- '''
def print_slot_machine(columns):
    # transpose the columns (flip or rotate to correct display orientation)
    # number of rows is based on the number of elements in each column
    for row in range(len(columns[0])):
        # loop trough the columns and only print the first value
        # use the enumerate() method to (ADD EXPLAINATION HERE)
        for i, column in enumerate(columns):
            # if the current item is not the last item in the list, print the pipe seperator
            if i != len(columns) -1:
                print(column[row], end=" | ")
            # otherwise dont print a pipe
            else:
                print(column[row], end="")
        print()


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


    ''' --- SPIN THE SLOTS --- '''
    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)

    ''' --- CALCULATE WINNINGS --- '''
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"These are your winning lines: ", *winning_lines)

# call the main() function to run everything
main()
