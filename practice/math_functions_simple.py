import math

# Given three floating-point numbers x, y, and z, 
# 1. output x to the power of z, 
# 2. x to the power of (y to the power of z), 
# 3. the absolute value of (x minus y), 
# 4. and the square root of (x to the power of z).

x = float(input())
y = float(input())
z = float(input()) 

val_one = math.pow(x, z)
val_two = math.pow(x, (math.pow(y, z)))
val_three = math.fabs(x - y)
val_four = math.sqrt(math.pow(x, z))

# Output each floating-point value with two digits after the decimal point
print(f"{val_one:.2f} {val_two:.2f} {val_three:.2f} {val_four:.2f}")