import math

radius = float(input()) 
height = float(input())

'''
Volume = πr2h
Area = 2πrh + 2πr2
'''
#print(math.pi)
#print(math.pow(radius, 2))

volume = math.pi * math.pow(radius, 2) * height
area = (2 * math.pi * radius * height) + (2 * math.pi * math.pow(radius, 2))

print(f"Volume: {volume:.1f} cubic inches")
print(f"Surface area: {area:.1f} square inches")
