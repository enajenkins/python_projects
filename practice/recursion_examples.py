'''Simple Recursion'''
    # The function calls itself directly and stops when a base case is reached.	
    # O(n) – due to n recursive calls	Easy to implement and understand	Factorial Calculation, Fibonacci Sequence
    # def func(n):	
       
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


'''Tail Recursion'''
# Recursion happens at the end of the function, which some languages optimize better, although Python lacks this optimization.	
# O(n) – linear recursive depth	Helps with some recursion optimizations	Summing Numbers, Accumulative Calculations	
	
# def func(n, acc):
def tail_factorial(n, acc=1):
    if n == 1:
        return acc
    return tail_factorial(n-1, n*acc)


'''Indirect Recursion'''
# Two or more functions call each other recursively.	
# O(n) – each function call depends on previous calls	Useful in complex logic scenarios	Alternating Patterns, Game Algorithms

# def func_a(n):   
def even(n):
    if n == 0:
        return True
    return odd(n - 1)
# def func_b(n):
def odd(n):
    if n == 0:
        return False
    return even(n - 1)



'''Helper Function'''
# Uses an inner helper function to maintain state or add additional parameters to simplify the main recursive call.	
# O(n) – each helper call adds to depth	Provides clearer logic and additional parameters	Factorial with Accumulator, Path Traversal	

# def func(n): 
def factorial(n):
    # def helper(n):
    def helper(n, acc):
        if n == 1:
            return acc
        return helper(n-1, n*acc)
    return helper(n, 1)


'''Nested Recursion'''	
# Recursive calls are made within the arguments of other recursive calls, causing complex recursive depth and multiple executions.	
# O(2^n) – recursive calls grow exponentially	Useful in some mathematical problems	Ackermann Function, Nested Operations

# def func(func(n)):	
def nested_rec(n):
    if n > 100:
        return n - 10
    return nested_rec(nested_rec(n+11))


'''Memoization'''	
# Stores previously computed results to avoid redundant recursive calls, reducing time complexity in certain cases.	
# O(n) – reduces repeated calculations by storing results	Optimizes performance for overlapping subproblems	Fibonacci Sequence, Dynamic Programming

# @lru_cache or memo = {}:	
from functools import lru_cache

@lru_cache(maxsize=None)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


'''Generator Recursion'''
# # Uses yield instead of return, producing an iterator rather than computing everything at once, useful for large data structures.	
# O(2^n) – similar to simple recursion if not memoized	Saves memory for large computations	Fibonacci Generator, Infinite Sequences	

# yield keyword:	
def gen_fib(n):
    if n <= 1:
        yield n
    else:
        yield from gen_fib(n - 1)
    yield from gen_fib(n - 2)


'''Mutual Recursion'''	
# Functions are split into two recursive calls, each calling the other (like a toggle), which is less common but useful in certain cases.	
# O(n) – single recursive depth for each call	Useful in scenarios with alternative conditions	Even/Odd Calculation, Alternating Logic Flows

# def func_a():
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

# def func_b():	 
def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)
