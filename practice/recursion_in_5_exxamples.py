#5 problems that are solved by different recursion solutions with varying levels of difficulty
'''
Recursion is a technique in computer science where a function calls itself as a subroutine. The function defines a base case, which is a condition that stops the recursive calls, and a recursive case, which makes the function call itself with a different input.

Recursion is a technique where a function calls itself in order to solve a problem. Recursion is a powerful tool for solving complex problems and can be used to solve problems in a more elegant and concise manner compared to an iterative approach. However, it is important to ensure that the base case is well defined, otherwise the recursion can go on indefinitely. Recursion is best used when the problem can be divided into smaller sub-problems of the same type and the solution to the larger problem can be constructed from the solutions of the sub-problems. The five problems solved by the code examples in this response are finding the factorial of a number, computing the nth Fibonacci number, finding the sum of elements in a list, reversing a string, and performing binary search.
'''

# Factorial of a number:
'''
The function takes in an integer n as input.
If n is equal to 1, the function returns 1, which serves as the base case.
If n is not equal to 1, the function returns n multiplied by the result of factorial(n - 1). This is the recursive case, where the function calls itself with an input of n - 1.

5 Use Cases:
    1. In mathematical modeling, factorials are used to calculate the number of permutations or combinations in a set.
    2. In combinatorics, factorials are used to calculate the number of ways to arrange items in a set.
    3. In probability and statistics, factorials are used to calculate the number of possible outcomes of a process.
    4. In computer algorithms, factorials are used to calculate the number of operations needed to solve a problem.
    5. In pharmaceutical research, factorials are used to calculate the number of different drug combinations that can be tested in a clinical trial.
'''

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Fibonacci series:
'''
The function takes in an integer n as input.
If n is equal to 0, the function returns 0, which serves as the first base case.
If n is equal to 1, the function returns 1, which serves as the second base case.
If n is greater than 1, the function returns the result of fibonacci(n - 1) added to the result of fibonacci(n - 2). This is the recursive case, where the function calls itself twice with inputs of n - 1 and n - 2.

5 Use Cases:
    1. In finance, the Fibonacci sequence is used to calculate the support and resistance levels of financial instruments.
    2. In computer graphics, the Fibonacci sequence is used to generate fractal patterns.
    3. In music theory, the Fibonacci sequence is used to determine the relationships between musical intervals.
    4. In biology, the Fibonacci sequence is used to describe the growth patterns of plants and animals.
    5. In cryptography, the Fibonacci sequence is used as a basic building block for many encryption algorithms.
'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



# Finding the n-th number in the Tower of Hanoi problem:
'''
Tower of Hanoi problem:
    In computer science, the Tower of Hanoi problem is a classic example of a recursive algorithm used to teach computer science students about recursion.
    In mathematics, the Tower of Hanoi problem is used to teach mathematical concepts such as algorithms, logic, and problem-solving skills.
    In engineering, the Tower of Hanoi problem is used to teach the principles of machine control and automation.
    In finance, the Tower of Hanoi problem is used to teach portfolio management and risk management concepts.
    In business, the Tower of Hanoi problem is used to teach decision-making, strategic planning, and problem-solving skills.
    Finding the n-th number in the Tower of Hanoi problem:
    In computer science, finding the n-th number in the Tower of Hanoi problem is a common exercise used to teach students about recursive algorithms.
    In mathematics, finding the n-th number in the Tower of Hanoi problem is used to teach mathematical concepts such as sequences and series.
    In engineering, finding the n-th number in the Tower of Hanoi problem is used to teach control systems and automation concepts.
    In finance, finding the n-th number in the Tower of Hanoi problem is used to teach portfolio management and risk management concepts.
    In business, finding the n-th number in the Tower of Hanoi problem is used to teach decision-making, strategic planning, and problem-solving skills.

The Function:
    The function takes in an integer n, and three strings source, auxiliary, and target, which represent the names of the towers in the Tower of Hanoi problem.
    If n is equal to 1, the function prints a message indicating that disk 1 should be moved from the source tower to the target tower. This serves as the base case.
    If n is greater than 1, the function first calls itself with n - 1 as the input, along with the source and target towers swapped. This moves the top n - 1 disks to the auxiliary tower.
    Then, the function prints a message indicating that disk n should be moved from the source tower to the target tower.
    Finally, the function calls itself again with n - 1 as the input, along with the auxiliary and source towers swapped, to move the n - 1 disks from the auxiliary tower to the target tower.
'''

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print("Move disk 1 from source", source, "to target", target)
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print("Move disk", n, "from source", source, "to target", target)
    tower_of_hanoi(n - 1, auxiliary, source, target)



# Reverse a string:
'''
The function takes in a string as input.
If the length of the string is 0, the function returns the string, which serves as the base case.
If the length of the string is greater than 0, the function returns the result of reverse_string(string[1:]) concatenated with the first character of the string, string[0]. This is the recursive case, where the function calls itself with a sub-string of the input string, excluding the first character.
'''

def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


# Binary search:
'''
The function takes in a sorted list arr, two integers low and high that represent the lower and upper bounds of the sub-list to be searched, and an integer x to be searched for.
If the lower bound is less than or equal to the upper bound, the function finds the midpoint of the sub-list.
If the element at the midpoint is equal to x, the function returns the index of the midpoint.
If the element at the midpoint is less than x, the function calls itself with mid + 1 as the new lower bound.
If the element at the midpoint is greater than x, the function calls itself with mid - 1 as the new upper bound.
If the lower bound is greater than the upper bound, the function returns -1, indicating that x was not found in the list.

5 Use Cases:
    1. In computer science, binary search is a fast and efficient algorithm for finding a specific element in a sorted list.
    2. In web development, binary search is used to find specific elements in a large dataset for display or processing.
    3. In finance, binary search is used to find specific financial instruments in a large database.
    4. In mathematics, binary search is used to find specific solutions to mathematical problems.
    5. In data analysis, binary search is used to find specific data points in a large dataset.

'''

def binary_search(arr, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    else:
        return -1



# Head recursion:
'''
Head Recursion: In head recursion, the recursive call is made before any processing is done in the current function. The result of the recursive call is then processed and returned.

Head recursion can be difficult to optimize and can result in stack overflow errors for large inputs.
'''
def printArray(arr, n):
    if n == 0:
        return
    print(arr[n - 1])
    printArray(arr, n - 1)


# Tail recursion:
'''
Tail Recursion: In tail recursion, the recursive call is the last statement executed in the function. This means that once the recursive call is executed, there is no further processing to be done in the current function. The function then returns the result of the recursive call.

Tail recursion can often be optimized by the compiler, resulting in improved performance.
'''
def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)


# 5 business cases for head or tail recursion:
'''
Data processing and analysis: 
    In businesses that deal with large amounts of data, both head and tail recursion can be used to process the data and generate meaningful insights. For example, a financial institution might use recursion to process large sets of data to identify trends in customer behavior.

Software development: 
    Recursion is a powerful tool in software development, and both head and tail recursion can be used in different parts of a software application. For example, a web application might use head recursion to traverse a tree-like data structure, while tail recursion could be used to perform mathematical calculations such as computing the factorial of a number.

Artificial intelligence and machine learning: 
    Recursion is a key technique in artificial intelligence and machine learning, and both head and tail recursion can be used in different algorithms. For example, a machine learning model might use head recursion to traverse a decision tree to make predictions, while tail recursion might be used to perform mathematical optimization.

Database management: 
    In database management, both head and tail recursion can be used to perform complex queries and transformations on large sets of data. For example, a database administrator might use head recursion to traverse a database tree to perform data normalization, while tail recursion might be used to perform mathematical calculations such as computing the factorial of a number.

Financial modeling and simulation: 
    In finance, both head and tail recursion can be used to model and simulate financial systems. For example, a financial analyst might use head recursion to simulate the behavior of a complex financial instrument, while tail recursion might be used to perform mathematical calculations such as computing the Fibonacci series.
'''
