'''
Write a recursive function called draw_triangle() that outputs lines of '*' to form an upside down isosceles triangle. Function draw_triangle() has one parameter, an integer representing the base length of the triangle. Assume the base length is always odd and less than 20. Output 9 spaces before the first '*' on the last line for correct formatting.

Hint: The number of '*' decreases by 2 for every line drawn.

Ex: If the input of the program is:

3
the function draw_triangle() outputs:

        ***
         *
Ex: If the input of the program is:

19
the function draw_triangle() outputs:

*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *
Note: No space is output before the first '*' on the first line when the base length is 19.
'''

# TODO: Write recursive draw_triangle() function here.


if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)
    