'''
Write a program that takes in a line of text as input, 
outputs that line of text in reverse. 
The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.
'''
 
# while there are user input values available
# check to make sure the user hasn't entered "Done", "done", or "d"
# if they have, then break the loop
# if they haven't reverse the list and print

while True:
    user_input = input()
    if user_input.lower() == "done" or user_input.lower() == "d":
        break
    else:
        print(user_input[::-1])

''' 
OUTPUT: 
ereht olleH
yeH
'''
