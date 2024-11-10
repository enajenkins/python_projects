# grab user input
user_input_string = input()

def is_palindrome(text_string):
    # declare a global var so it can be accessed outside of the function
    global answer
    
    # normalize the string so you can perform a comparison
        # "".join() can take an iterable that can filter each character - then concatenate it back into a string with no whitespaces
        # make the string case insensitive for proper comparison
        # loop through all the remaining characters checking to ensure that it's a number or letter
    initial_string = "".join(char.lower() for char in text_string if char.isalnum())
    
    # reverse the string for the item to compare the initial string to
    reversed_string = initial_string[::-1]
    #print(initial_string)
    #print(reversed_string)
    
    # compare the strings
    if initial_string == reversed_string:
        answer = True
    else:
        answer = False
        return answer

is_palindrome(user_input_string)    

if answer == True:
    print(f"{user_input_string} is a palindrome")
else:
    print(f"{user_input_string} is not a palindrome")
