#######################################################################################################################################
# Title: library
# Author: Tony Pescatore
# Description: Library will provide functions that will be called in main.py
#######################################################################################################################################

# Constant
TO_INT_FAIL = 'F'

# Welcome message for start of calc
def welcome_mess():
    # Open welcome mmessage file
    with open('Headers/welcome_message.txt') as header_file:
        # Spacing cleanup
        print('\n')
        # Print welcome banner
        for line in header_file:
            print(line, end='')
        # Spacing cleanup
        print('\n')
    print('Hello, welcome to the Stardew Valley Crop Calculator! This tool can help you with all your Stardew Valley Calculations.')

# Displays info calculated for the user with crop calculation
# seeds_needed = number of seeds needed to plant in all usable tiles (INT - Checked when user enters or it is calculated in-house)
# fertilizer = Fertilizer object which was selected by user
# crop = Crop object which was selected by user
def display_info(seeds_needed, fertilizer, crop):
    cost = calc_cost(seeds_needed, fertilizer, crop)
    print(f'You need ${cost} gold to fully plant your field for this season!')

# Thanks user for using calculator
def thank_you_mess():
    print('Thank you for using my Stardew Valley Crop Calculator!')
    input("Press Enter to exit...")
    # Open goodbye mmessage file
    with open('Headers/exit_message.txt') as footer_file:
        # Print welcome banner
        for line in footer_file:
            print(line, end='')
        # Spacing cleanup
        print('\n')

# Calculates the cost of buying all the crops and fertilizer for the field
# seeds_needed = number of seeds needed to plant in all usable tiles (INT - Checked when user enters or it is calculated in-house)
# fertilizer = Fertilizer object which was selected by user
# crop = Crop object which was selected by user
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

# Determines what the user would like our app to do (Crop/field Calc, Crafting calc, cooking calc[WIP] )
# Returns String of calculator to be run
def get_task():
    # List of all current tasks app can do
    task_list = ['Crop Field Calculator', 'Crafting Calculator']
    print('From the following options please pick which calculator you would like to use:')
    while True:
        for i in range(1, len(task_list)+1):
            print('{}. {}'.format(i, task_list[i-1]))
            
        # Repeats request for task response until it gets a valid response
        try:
            task_res = int(input('Please enter the number corresponding to the calculator you would like to use: ').strip())
            if task_res <= 0 or task_res >= (len(task_list)+1):
                int(TO_INT_FAIL)
            break
        except:
            print('Invalid resposnse. Please enter a whole number from the range provided.')
            
    print(task_list[task_res-1])
    return task_list[task_res-1]