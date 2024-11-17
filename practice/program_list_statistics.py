'''
Program Specifications Write a program to calculate the minimum, maximum, mean, median, mode, and whether a list is a palindrome.

Note: This program is designed for incremental development. Complete each step and submit for grading before starting the next step. Only a portion of tests pass after each step but confirm progress.

Step 0. Review the template code. A list is filled with integers from standard input.

Step 1 (2 pts). Use a loop to determine and output the minimum and maximum values in the list. Submit for grading to confirm one test passes.

Ex: If input is:

4 1 5 4 99 17
the output is:

Minimum: 1
Maximum: 99
Step 2 (2 pts). Sum all list elements and calculate the mean (or average). Output the mean with one decimal place using print(f"Mean: {mean:.1f}").

Ex: If input is:

4 1 5 4 99 17
the output is:

Minimum: 1
Maximum: 99
Mean: 21.7
Step 3 (2 pts). Use a loop to determine if the list is a palindrome, meaning values are the same from front to back and back to front. Output "True" or "False". Submit for grading to confirm three tests pass.

Ex: If input is:

1 2 3 4 5 4 3 2 1
the output is:

Minimum: 1
Maximum: 5
Mean: 2.8
Palindrome: True
Step 4 (1 pt). The template code includes a call to sort(), which sorts the list elements into ascending order. Do not sort the list before step 4. After sorting, identify the median. The median is located in the middle of the list if the list's length is odd. Otherwise, the median is the average of the middle two values. Output the median with one decimal place. Submit for grading to confirm four tests pass.

Ex: If input is:

2 2 5 6 7 7
the output is:

Minimum: 2
Maximum: 7
Mean: 4.8
Palindrome: False
Median: 5.5
Step 5 (3 pts). Challenging! Identify the mode after the list is sorted in ascending order. The mode is the value that appears most frequently. Assume only one mode exists. Hint: Use a loop to process each list element, looking for the longest sequence of identical values. Submit for grading to confirm all tests pass.

Ex: If input is:

1 2 2 2 3 3 4 5 6
the output is:

Minimum: 1
Maximum: 6
Mean: 3.1
Palindrome: False
Median: 3.0
Mode: 2

'''