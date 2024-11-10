'''
Given the number of people attending a pizza party, output the number of needed pizzas and total cost. For the calculation, assume that people eat 2 slices on average and each pizza has 12 slices and costs $14.95.
'''

import math

people_attending = int(input())
slices_per_person = 2
slices_per_pizza = 12
price_per_pizza = 14.95

pizzas_needed = math.ceil((people_attending * slices_per_person) / slices_per_pizza)
total_cost = pizzas_needed * price_per_pizza

print(f"Pizzas: {pizzas_needed}")
print(f"Cost: ${total_cost:.2f}")
