#######################################################################################################################################
# Title: main
# Author: Tony Pescatore
# Description: Main will utilize functions from library.py and inputs from the user to generate the cost of planting all your crops.
#######################################################################################################################################

# Imports
import library as lib
from fertilizer import get_fertilizer_used
from crop import get_crop_selection
from sprinkler import seeds_to_buy

def main():
    # welcome
    lib.welcome_mess()

    # How many crops can be grown
    #total_seeds = seeds_to_buy()

    # Ask for fertilizers used
    #fertilizer = get_fertilizer_used()

    # Get crop info
    #crop = get_crop_selection()

    # display information to user
    #lib.display_info(total_seeds, fertilizer, crop)

    # Exit message
    lib.thank_you_mess()

main()