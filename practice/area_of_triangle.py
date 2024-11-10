import math

#Get the sides of the triangle
a = float(input())
b = float(input())
c = float(input())
tri_perimeter = (a + b + c)

'''
Heron's Formula
s = half of the triangle's perimeter
area = the square root of s(s-a)(s-b)(s-c), where a, b, and c are each sides of the triangle.
'''
s = (tri_perimeter) / 2
area = math.sqrt(s * (s-a) * (s-b) * (s-c))

print(f"The area of the triangle is: {area:.3f}")