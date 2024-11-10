'''
In main.py define the Product class that will manage product inventory. Product class has three attributes: a product code, the product's price, and the number count of product in inventory.

Implement the following methods:

A constructor with 3 parameters that sets all 3 attributes to the value in the 3 parameters
set_code(self, code) - set the product code (i.e. SKU234) to parameter code
get_code(self) - return the product code
set_price(self, price) - set the price to parameter price
get_price(self) - return the price
set_count(self, count) - set the number of items in inventory to parameter count
get_count(self) - return the count
add_inventory(self, amt) - increase inventory by parameter amt
sell_inventory(self, amt) - decrease inventory by parameter amt
Ex. If a new Product object is created with code set to "Apple", price set to 0.40, and the count set to 3, the output is:

Name: Apple
Price: 0.40
Count: 3
Ex. If 10 apples are added to the Product object's inventory, but then 5 are sold, the output is:

Name: Apple
Price: 0.40
Count: 8
Ex. If the Product object's code is set to "Golden Delicious", price is set to 0.55, and count is set to 4, the output is:

Name: Golden Delicious
Price: 0.55
Count: 4
'''

class Product:
    # Type your code here

    if __name__ == "__main__":
        name = 'Apple'
        price = 0.40
        num = 3
        p = Product(name, price, num)

        # Test 1 - Are instance attributes set/returned properly?
        print('Name:', p.get_code())
        print(f'Price: {p.get_price():.2f}')
        print('Count:', p.get_count())

        # Test 2 - Are attributes set/returned properly after adding and selling?
        num = 10
        p.add_inventory(num)
        num = 5
        p.sell_inventory(num)
        print('Name:', p.get_code())
        print(f'Price: {p.get_price():.2f}')
        print('Count:', p.get_count())

        # Test 3 - Do setters work properly?
        name = 'Golden Delicious'
        p.set_code(name)
        price = 0.55
        p.set_price(price)
        num = 4
        p.set_count(num)
        print('Name:', p.get_code())
        print(f'Price: {p.get_price():.2f}')
        print('Count:', p.get_count())