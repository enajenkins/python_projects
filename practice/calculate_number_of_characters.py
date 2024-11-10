''' 1) Prompt the user to enter a string of their choosing. Output the string. '''
input_str = input("Enter a sentence or phrase:\n")
    
'''
(2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string. 
We encourage you to use a for loop in this function
'''
def get_num_of_characters(n):
    count = 0
    # for every character in the value passed to n, update the count by 1
    for char in n:
        count += 1
    return count


# (4) Extend the program further by implementing the output_without_whitespace() function. 
def output_without_whitespace(x):
    new_string = ""
    # for every character in the value passed to x, print the character - all on the same line
    for char in x:
        if not char.isspace():
            new_string += char
    return new_string

if __name__ == '__main__':
    print()
    print("You entered:", input_str)
    print()
    # (3) Extend the program by calling the get_num_of_characters() function and then output the returned result.
    print("Number of characters:",  get_num_of_characters(input_str))
    # (4)
    print("String with no whitespace:", output_without_whitespace(input_str))
