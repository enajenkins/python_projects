'''
Program Specifications Write a program to search three parallel lists containing customer credit card debt information. Identify statistics such as the number of customer names that begin with "Sm", the number of customers with no debt, and the number of customers that live in a specific state.

Note: This program is designed for incremental development. Complete each step and submit for grading before starting the next step. Only a portion of tests pass after each step but confirm progress.

Step 0. Review the starter code in the main portion of the program. The number of requested customers is input (integer). Function read_customer_data() is called that reads data from a text file and fills three parallel lists with customer names, state of residence, and amount of credit card debt for each customer. Using a function is a convenient way to fill lists with hundreds of elements. Functions and reading data from text files are described in other sections of the book.

Step 1. Input a debt limit (integer), search phrase (string), and state abbreviation (string). Note that the number of customers to consider is already input during Step 0.

Step 2 (2 pts). Use a loop to process each element of the names and debt lists to identify the customer with the highest debt. Output a report header, number of customers, and the person's name with the highest debt. Submit for grading to confirm two tests pass.

Ex: If input is:

1000 
250 
P 
LA
the output is:

U.S. Report
Customers: 1000
Highest debt: Sullivan
Step 3 (2 pts). Use a loop to process each element of the names list to count all customer names that begin with the specified search phrase. Ex: How many customer names begin with "Bre" or "L"? Hint: Use the startswith() function. Output the number of customer names that start with the search phrase. Submit for grading to confirm four tests pass.

Ex: If input is:

5000 
8000 
Mor
CA
the output is:

U.S. Report
Customers: 5000
Highest debt: Smith
Customer names that start with "Mor": 45
Step 4 (2 pts). Use a loop to process each element of the names and debt lists to count the number of customers that have debt higher than the specified debt limit and the number of customers that have no debt. Output all results. Submit for grading to confirm six tests pass.

Ex: If input is:

1500
1000
R
WY
the output is:

U.S. Report
Customers: 1500
Highest debt: Sullivan
Customer names that start with "R": 90
Customers with debt over $1000: 1176
Customers debt free: 324
Step 5 (4 pts). Repeat steps 2 - 4 for all customers living in the specified state. Output all results including a header for the state report. Submit for grading to confirm all tests pass.

Ex: If input is:

2500
5000
K
TX
the output is:

U.S. Report
Customers: 2500
Highest debt: Sullivan
Customer names that start with "K": 71
Customers with debt over $5000: 1280
Customers debt free: 543

TX Report
Customers: 196
Highest debt: Dobbs
Customer names that start with "K": 5
Customers with debt over $5000: 110
Customers debt free: 43

'''

def read_customer_data(filename):
    """Read and return data from filename as a list of lists (name, state, debt)"""
    names = []
    states = []
    debts = []

    with open(filename) as f:
        rows = f.readlines()
    for row in rows:
        row = row.split(',')
        names.append(row[0])
        states.append(row[1])
        debts.append(float(row[2].strip()))
    return names, states, debts

# Main portion of the program
if __name__ == '__main__':
    # number of rows to consider
    num_customers = int(input())

    names, states, debts = read_customer_data("CustomerData.csv")

    # Type your code here.
