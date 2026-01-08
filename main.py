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
from craftable import crafting_calculator
from cooking import cooking_calculator

def main():
    # Welcome
    lib.welcome_mess()
    # While True for looping if user wants to try again
    while True:
        # Get task to be done
        task = lib.get_task()
        #print(task)

        # Match task to task path
        match task:
            case 'Crop Field Calculator':
                print('\nCrop Field Calculator:')
                # How many crops can be grown
                total_seeds = seeds_to_buy()

                # Ask for fertilizers used
                fertilizer = get_fertilizer_used()

                # Get crop info
                crop = get_crop_selection()

                # Display information to user
                lib.display_info(total_seeds, fertilizer, crop)
            
            case 'Crafting Calculator':
                print('\nCrafting Calculator:')
                crafting_calculator()
            
            case 'Cooking Calculator':
                print('\nCooking Calculator:')
                cooking_calculator()
        
        # See if user wishes to run the calculator again
        while True:
            try:
                try_again_res = (input('\nWould you like to try another calculator? Please enter yes or no: ').lower()).strip()
                if try_again_res == 'yes' or try_again_res == 'no':
                    break
                else:
                    int(lib.TO_INT_FAIL)
            except:
                print('Invalid response, please respond with yes or no.')
        # Breaks loop if user is done
        if try_again_res == 'no':
            break

    # Exit message
    lib.thank_you_mess()

main()