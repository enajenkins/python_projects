'''
Write a program that reads integers user_num and div_num as input, 
and output the quotient (user_num divided by div_num). 
Use a try block to perform all the statements. 
Use an except block to catch any ZeroDivisionError and output an exception message. 
Use another except block to catch any ValueError caused by invalid input and output an exception message.

Note: ZeroDivisionError is thrown when a division by zero happens. 
ValueError is thrown when a user enters a value of different data type than what is defined in the program. 
Do not include code to throw any exception in the program.
'''

try:
    # get user values
    user_num = int(input())
    div_num = int(input())
    
    # get an integer from the quotient of the entered values
    quotient = user_num // div_num
    
    # display it
    print(quotient)
    
except ZeroDivisionError as err:
    print(f"Zero Division Exception: {err}")
    
except ValueError as err:
    print(f"Input Exception: {err}")