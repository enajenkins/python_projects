'''
Output the first integer and subsequent increments of 5 
as long as the value is less than or equal to the second integer. 
End with a newline
'''

int_1 = int(input())
int_2 = int(input())

if int_1 <= int_2:
    while int_1 <= int_2:
        print(int_1, end=" ")
        int_1 += 5
    print()
else:
    print("Second integer can't be less than the first.")