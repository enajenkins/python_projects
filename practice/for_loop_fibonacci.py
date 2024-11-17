def fibonacci(n):
    # Any negative index values should return -1
    if n < 0:
        return -1
    # The Fibonacci sequence begins with 0 and then 1 follows
    # Cannot calculate the rest without the first two numbers - which are always 0 and 1
    if n == 0:
        return 0
    if n == 1:
        return 1
 
    # All subsequent values are the sum of the previous two
    # Declare vars to temporarily store the previous two Fib numbers and start the loop with values
    a = 0
    b = 1
    
    # range(start, stop) generates a sequence of numbers often used for iteration in loops (not indexed)
    # the range will go up to (but not including) stop point, so you need to add +1 (think length but numbers start at 0)
    for i in range(2, n + 1):
        '''
        Simultaneous Assignment (a, b = b, a + b):
        is a Python-specific feature where you can assign multiple variables at the same time.
        the previous value of b is assigned to a first, 
        and then b is updated using the original values of a and b in one step.
            *a is assigned the current value of b.
            *b is assigned the sum of the original values of a and b.
            *This ensures the correct update of the variables needed for the Fibonacci sequence.

        Python evaluates the right-hand side first before performing the assignment.
        This means that the new values of a and b are assigned simultaneously, 
        allowing you to use the original values of both variables to calculate the next Fibonacci number.
        This ensures the correct calculation of the Fibonacci sequence.
        '''
        a, b = b, a + b 
    return b
        


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')