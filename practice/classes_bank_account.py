'''
Build a class called BankAccount that manages checking and savings accounts. The class has three attributes: a customer name, the customer's savings account balance, and the customer's checking account balance.

Implement the following constructor and instance methods as listed below:

Constructor with parameters (self, new_name, checking_balance, savings_balance) - set the customer name to parameter new_name, set the checking account balance to parameter checking_balance, and set the savings account balance to parameter savings_balance.
deposit_checking(self, amount) - add parameter amount to the checking account balance (only if positive)
deposit_savings(self, amount) - add parameter amount to the savings account balance (only if positive)
withdraw_checking(self, amount) - subtract parameter amount from the checking account balance (only if positive)
withdraw_savings(self, amount) - subtract parameter amount from the savings account balance (only if positive)
transfer_to_savings(self, amount) - subtract parameter amount from the checking account balance and add to the savings account balance (only if positive)
'''

# TODO: Define BankAccount class
    # TODO: Define constructor with parameters to initialize instance attributes
    
    # TODO: Define deposit_checking()
    
    # TODO: Define deposit_savings()
    
    # TODO: Define withdraw_checking()
    
    # TODO: Define withdraw_savings()
    
    # TODO: Define transfer_to_savings()

if __name__ == "__main__":
    account = BankAccount("Mickey", 500.00, 1000.00)
    account.checking_balance = 500
    account.savings_balance = 500
    account.withdraw_savings(100)
    account.withdraw_checking(100)
    account.transfer_to_savings(300)

    print(account.name)
    print(f'${account.checking_balance:.2f}')
    print(f'${account.savings_balance:.2f}')