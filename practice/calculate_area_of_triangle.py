''' Heron's Formula:

Heron's formula is a mathematical equation used to calculate the area of a triangle when the lengths of all three sides are known. The formula is named after Hero of Alexandria, a Greek engineer and mathematician. The formula in Python is:

math.sqrt(s * (s - a) * (s - b) * (s - c))

where  𝐴 A is the area of the triangle,  𝑎 a,  𝑏 b, and  𝑐 c are the lengths of the sides of the triangle, and  𝑠 s is the semi-perimeter of the triangle, calculated as:

s = (a + b + c) / 2

This formula is particularly useful because it does not require knowing the angles of the triangle, only the lengths of its sides.

Use Cases for Heron's Formula

!. Land Surveying and Real Estate: Heron's formula is used in land surveying to determine the area of irregular parcels of land. When a plot of land cannot be easily divided into simple shapes like rectangles or circles, surveyors can divide the plot into triangles, measure the sides, and use Heron's formula to calculate the area of each triangle. The sum of these areas gives the total area of the plot, helping in calculations related to property valuation, sales, or development.

2. Architecture and Construction: In the design and construction of buildings and structures, Heron's formula can be used to calculate the areas of triangular components such as trusses, roofs, or other architectural features. Knowing these areas helps in estimating materials costs and ensuring structural stability. It is also used in the creation of curved surfaces where multiple triangular elements might be involved.
'''

# Get access to the math module functions
import math


# Get the sides of the triangle from user inputs
a = float(input())
b = float(input())
c = float(input())
tri_perimeter = (a + b + c)


# s = half of the triangle's perimeter
s = (tri_perimeter) / 2

# area = the square root of s(s-a)(s-b)(s-c), where a, b, and c are each sides of the triangle.
area = math.sqrt(s * (s-a) * (s-b) * (s-c))


print(f"The area of the triangle is: {area:.3f}")