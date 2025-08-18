#######################################################################################################################################
# Title: library
# Author: Tony Pescatore
# Description: Library will provide functions that will be called in main.py
#######################################################################################################################################

# Constant
TO_INT_FAIL = 'F'

# Welcome message for start of calc
def welcome_mess():
    print('Hello, welcome to the Stardew Valley Crop Calculator! This tool will help you determine how much it will cost for you to fully plant and fertilize your farm.')

# Displays info calculated for the user
def display_info(seeds_needed, fertilizer, crop):
    cost = calc_cost(seeds_needed, fertilizer, crop)
    print(f'You need ${cost} gold to fully plant your field for this season!')

# Thanks user for using calc
def thank_you_mess():
    print('Thank you for using my Stardew Valley Crop Calculator!')
    input("Press Enter to exit...")

# Calculates the cost of buying all the crops and fertilizer for the field
def calc_cost(seeds_needed, fertilizer, crop):
    if fertilizer.price == 0:   # craftable fertilizer
        min_crafts = int(int(seeds_needed)/fertilizer.amt_per_craft) + bool(int(seeds_needed)/fertilizer.amt_per_craft%1)
        for item in fertilizer.recipe:
            temp_material_needed = min_crafts * item[1]
            print(f'You need {temp_material_needed} {item[0]}(s) for fertilizer.')
        total_cost = ((crop.seed_price) * int(seeds_needed))
    else:
        total_cost = ((crop.seed_price) + (fertilizer.price)) * int(seeds_needed)

    return total_cost