'''
In the file main.py write a class called Calculator that emulates basic functions of a calculator: add, subtract, multiply, divide, and clear. The class has one attribute called value for the calculator's current value. Implement the following methods as listed below:

Default constructor method to set the attribute to 0.0
add(self, val) - add the parameter to the attribute
subtract(self, val)- subtract the parameter from the attribute
multiply(self, val) - multiply the attribute by the parameter
divide(self, val)- divide the attribute by the parameter
clear(self) - set the attribute to 0.0
get_value(self) - return the attribute
Given two float input values num1 and num2, the program outputs the following values:

The initial value of the instance attribute, value
The value after adding num1
The value after multiplying by 3
The value after subtracting num2
The value after dividing by 2
The value after calling the clear() method
Ex: If the input is:

10.0 
5.0
the output is:

0.0
10.0
30.0
25.0
12.5
'''

class Calculator:

    # Type your code here.

    if __name__ == "__main__":

        calc = Calculator()
        num1 = float(input())
        num2 = float(input())

        # 1. The initial value
        print(f'{calc.get_value():.1f}')

        # 2. The The value after adding num1
        calc.add(num1)
        print(f'{calc.get_value():.1f}')

        # 3. The value after multiplying by 3
        calc.multiply(3)
        print(f'{calc.get_value():.1f}')

        # 4. The value after subtracting num2
        calc.subtract(num2)
        print(f'{calc.get_value():.1f}')

        # 5. The value after dividing by 2
        calc.divide(2)
        print(f'{calc.get_value():.1f}')

        # 6. The value after calling the clear() method
        calc.clear()
        print(f'{calc.get_value():.1f}')