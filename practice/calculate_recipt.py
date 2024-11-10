# FIXME (1): Finish reading item price and quantity, then output a receipt
'''
Prompt the user to input a food item name, price, and quantity.
Output an itemized receipt.
'''
item_1_name = input('Enter food item name:\n')
item_1_price = float(input('Enter item price:\n'))
item_1_quantity = float(input('Enter item quantity:\n\n'))

total_item_1_cost = item_1_price * item_1_quantity
total_cost = total_item_1_cost

print("RECEIPT")
print(f"{int(item_1_quantity)} {item_1_name} @ ${item_1_price:.2f} = ${total_item_1_cost:.2f}")
print(f"Total cost: ${total_cost:.2f}\n\n")



   
# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt

item_2_name = input('Enter second food item name:\n')
item_2_price = float(input('Enter item price:\n'))
item_2_quantity = float(input('Enter item quantity:\n\n'))

total_item_2_cost = item_2_price * item_2_quantity
total_cost = total_item_1_cost + total_item_2_cost

print("RECEIPT")
print(f"{int(item_1_quantity)} {item_1_name} @ ${item_1_price:.2f} = ${total_item_1_cost:.2f}")
print(f"{int(item_2_quantity)} {item_2_name} @ ${item_2_price:.2f} = ${total_item_2_cost:.2f}")
print(f"Total cost: ${total_cost:.2f}\n")



   
# FIXME (3): Add a gratuity and total with tip to the second receipt

tip = (total_cost * (15/100))

print(f"15% gratuity: ${tip:.2f}")
print(f"Total with tip: ${total_cost + tip:.2f}")
