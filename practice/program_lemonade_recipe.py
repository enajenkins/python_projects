# FIXME (1): Finish reading other items into variables, then output the three ingredients
'''
Prompt the user for the number of cups of lemon juice, water, and agave nectar needed to make lemonade.
Prompt the user to specify the number of servings the recipe yields.
Output the ingredients and serving size.
'''
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input("Enter amount of water (in cups):\n"))
agave_nectar_cups = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n\n"))

print(f"Lemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water_cups:.2f} cup(s) water")
print(f"{agave_nectar_cups:.2f} cup(s) agave nectar\n")


# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
'''
Prompt the user to specify the desired number of servings.
Adjust the amounts of each ingredient accordingly.
Output the ingredients and serving size.
'''

desired_servings = float(input("How many servings would you like to make?\n\n"))

adjustment_multiplier = desired_servings / servings
updated_lemon_juice_cups = lemon_juice_cups * adjustment_multiplier
updated_water_cups = water_cups * adjustment_multiplier
updated_agave_nectar_cups = agave_nectar_cups * adjustment_multiplier

print(f"Lemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{updated_lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{updated_water_cups:.2f} cup(s) water")
print(f"{updated_agave_nectar_cups:.2f} cup(s) agave nectar\n")


# FIXME (3): Convert and output the ingredients from (2) to gallons
'''
Convert the ingredient measurements from (2) to gallons.
Output the ingredients and serving size.
Note: There are 16 cups in a gallon.
'''

cups_in_gallon = 16
print(f"Lemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{updated_lemon_juice_cups / cups_in_gallon:.2f} gallon(s) lemon juice")
print(f"{updated_water_cups / cups_in_gallon:.2f} gallon(s) water")
print(f"{updated_agave_nectar_cups / cups_in_gallon:.2f} gallon(s) agave nectar")