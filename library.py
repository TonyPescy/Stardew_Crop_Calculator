#######################################################################################################################################
# Title: library
# Author: Tony Pescatore
# Description: Library will provide functions that will be called in main.py
#######################################################################################################################################

# Imports
from crop import Crop
from sprinkler import get_number_of_sprinklers, get_number_of_nozzles, get_number_of_blocked_tiles, generate_sprinklers

# Welcome message for start of calc
def welcome_mess():
    print('Hello, welcome to the Stardew Valley Crop Calculator! This tool will help you determine how much it will cost for you to fully plant and fertilize your farm.')

# 
def display_info():
    print('NAN')

# Thanks user for using calc
def thank_you_mess():
    print('Thank you for using my Stardew Valley Crop Calculator!')

# Using functions from sprinkler.py this will determine how many seeds the user will need to plant their whole field
def seeds_to_buy():
    seeds_needed = 0
    known_seeds_res = ''
    valid_res = False
    while known_seeds_res != 'yes' and known_seeds_res != 'no':
        known_seeds_res = (input('Do you know how many seeds you need for your entire field? Please respond with "Yes" or "No": ').lower()).strip()

        if known_seeds_res == 'yes':
            # Asks for user value of seeds until it gets a valid integer from user
            while valid_res == False:
                seeds_needed = input('Please enter the number of seeds you need to buy: ')
                try:
                    if int(seeds_needed) <= 0:
                        print('Please enter a number larger than 0 to proceed.')
                    else:   # Only way to exit while - Valid entry provided by user
                        print('Valid User input!')
                        valid_res = True
                        break
                except:
                    print('Invalid value for number of seeds needed. Please enter a postive integer for number of seeds needed.')

        elif known_seeds_res == 'no':
            # Asks user for info on sprinkler types and quantity, pressure nozzles, and anything blocking potential crop locations. Then calcs number of seeds needed for their field
            print('We will now try to calculate how many seeds you will need for your field. Please answer the following questions with whole numbers.')

            # Sprinkler Section
            nums_of_spr_list = get_number_of_sprinklers() # list order is spirnkler, quality, iridium

            # Pressure Nozzle Section
            press_noz = get_number_of_nozzles()
            print('Note: Pressure nozzles will be applied on Iridium Sprinklers first, then Quality Sprinklers, and Sprinklers last for our calculations as that is the most efficient use of them.')

            # Unusable Tile Section
            blocked_tiles = get_number_of_blocked_tiles()

            # Calaulation Section
            sprinkler_stat_list = generate_sprinklers()

            if press_noz == 0:
                seeds_needed += nums_of_spr_list[2]*sprinkler_stat_list[2].tiles_watered    # iridium sprinklers added to total
                seeds_needed += nums_of_spr_list[1]*sprinkler_stat_list[1].tiles_watered    # quality sprinklers added to total
                seeds_needed += nums_of_spr_list[0]*sprinkler_stat_list[0].tiles_watered    # sprinklers added to total
            else:
                sprinkler_total = nums_of_spr_list[2] + nums_of_spr_list[1] + nums_of_spr_list[0]
                n = 2   # Initial value to determine sprinkler being used in for loop
                while sprinkler_total > 0:
                    for i in range(nums_of_spr_list[n]):

                        if press_noz > 0:
                            seeds_needed += sprinkler_stat_list[n].tiles_with_nozzle
                            press_noz -= 1
                            sprinkler_total -= 1
                        else:
                            seeds_needed += sprinkler_stat_list[n].tiles_watered
                            sprinkler_total -= 1
                    
                    # update n for next sprinkler
                    n -= 1
                if press_noz > 0:
                    print('You have ' + str(press_noz) + ' pressure nozzle(s) left. You should craft more sprinklers if you are able to!')
        else:
            # Invalid respone for known_seeds_res
            print('Invalid response, please enter "Yes" or "no".')
            
    seeds_needed -= blocked_tiles
    return seeds_needed