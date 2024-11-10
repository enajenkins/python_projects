# Write a program that reads integers user_num and div_num as input, 
# and outputs user_num divided by div_num three times using floor divisions.

user_num = int(input())
div_num = int(input())

first_out = user_num // div_num
second_out = first_out // div_num
third_out = second_out // div_num

print(first_out, second_out, third_out)
