'''
Write a program with total change amount as an integer input, 
output the change using the fewest coins, one coin type per line.
The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies.
Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.
'''
total_change_amt = int(input())
 
num_dollars = total_change_amt // 100
num_quarters = (total_change_amt - (num_dollars * 100)) // 25
num_dimes = ((total_change_amt - (num_dollars * 100)) % 25) // 10
num_nickels = (((total_change_amt - (num_dollars * 100)) % 25) % 10) // 5
num_pennies = total_change_amt % 5

    
if num_dollars == 1:
    print(f"{num_dollars} Dollar")
if num_dollars > 1:
    print(f"{num_dollars} Dollars")
    
if num_quarters == 1:
    print(f"{num_quarters} Quarter")
if num_quarters > 1:
    print(f"{num_quarters} Quarters")
    
if num_dimes == 1:
    print(f"{num_dimes} Dime")
if num_dimes > 1:
    print(f"{num_dimes} Dimes")
    
if num_nickels == 1:
    print(f"{num_nickels} Nickel")
if num_nickels > 1:
    print(f"{num_nickels} Nickels")
    
if num_pennies == 1:
    print(f"{num_pennies} Penny")
if num_pennies > 1:
    print(f"{num_pennies} Pennies")
    
if num_dollars < 1 and  num_quarters < 1 and  num_dimes < 1 and  num_nickels < 1 and  num_pennies < 1:
    print("No change")
