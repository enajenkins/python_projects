'''
Write a recursive function called digit_count() that takes a positive integer as a parameter and returns the number of digits in the integer. Hint: The digit count increases by 1 whenever the input number is divided by 10.

Ex: If the input is:

345
the function digit_count() returns and the program outputs:

3
'''

# TODO: Write recursive digit_count() function here.

if __name__ == '__main__':
    num = int(input())
    digit = digit_count(num)
    print(digit)