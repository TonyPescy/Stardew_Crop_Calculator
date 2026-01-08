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
    # If an invalid field size was calculated
    if seeds_needed <= 0:
        print('Your field size was invalid based on the calculations, please try again!')
    else:
        cost = calc_cost(seeds_needed, fertilizer, crop)
        print('\nYou need {} gold to fully plant your field with {} {} seeds for {}!'.format(cost, seeds_needed, crop.name, crop.season))
        if fertilizer.price != 0:
            print('You need {} gold to fully fertilize your field with {}.'.format(fertilizer.price*seeds_needed, fertilizer.name))
            print('Total gold needed: {} + {} = {}'.format(cost, fertilizer.price*seeds_needed, (fertilizer.price*seeds_needed)+cost))


# Thanks user for using calculator
def thank_you_mess():
    print('\nThank you for using my Stardew Valley Crop Calculator!')
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
        print('\n{} Recipe:'.format(fertilizer.name)) # Formatting cleanup
        for item in fertilizer.recipe:
            temp_material_needed = min_crafts * item[1]
            print(f'\t{temp_material_needed} {item[0]}(s)')
        total_cost = ((crop.seed_price) * int(seeds_needed))
        
    else:
        total_cost = (crop.seed_price) * int(seeds_needed)

    return total_cost

# Determines what the user would like our app to do (Crop/field Calc, Crafting calc, cooking calc, artisan item calc[WIP] )
# Returns String of calculator to be run
def get_task():
    # List of all current tasks app can do
    task_list = ['Crop Field Calculator', 'Crafting Calculator', 'Cooking Calculator']
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
            
    #print(task_list[task_res-1])
    return task_list[task_res-1]