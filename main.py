###########################################################################################################################################
# Title: main
# Author: Tony Pescatore
# Description: Main will utilize functions from other .py files and inputs from the user to generate the cost of planting all your crops.
###########################################################################################################################################

# Imports
import library as lib
from fertilizer import get_fertilizer_used
from crop import get_crop_selection
from sprinkler import seeds_to_buy
#from craftable import 

from craftable import read_recipe_csv

def main():
    # Welcome
    lib.welcome_mess()

    # Get task to be done
    task = lib.get_task()
    print(task)

    # Match task to task path
    match task:
        case 'Crop Field Calculator':
            # How many crops can be grown
            total_seeds = seeds_to_buy()

            # Ask for fertilizers used
            fertilizer = get_fertilizer_used()

            # Get crop info
            crop = get_crop_selection()

            # Display information to user
            lib.display_info(total_seeds, fertilizer, crop)
        
        case 'Crafting Calculator':
            print('CRAFTING CALC FOUND!')
            # Get users crafting item type
            

# TESTER
#    test1 = read_recipe_csv('Artisan Equipment')
#    print(test1)

    # Exit message
    lib.thank_you_mess()

main()