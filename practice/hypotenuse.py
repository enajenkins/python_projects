import math

side_1_len = float(input())
side_2_len = float(input()) 
hypotenuse = math.hypot(side_1_len, side_2_len)
print(f"Hypotenuse: {hypotenuse:.2f}")