'''
Write a recursive function called print_num_pattern() to output the following number pattern.

Given a positive integer as input (Ex: 12), subtract another positive integer (Ex: 3) continually until a negative value is reached, and then continually add the second integer until the first integer is again reached. For this lab, do not end output with a newline.

Do not modify the given main program.

Ex. If the input is:

12
3
the output is:

12 9 6 3 0 -3 0 3 6 9 12 
'''

# TODO: Write recursive print_num_pattern() function

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)