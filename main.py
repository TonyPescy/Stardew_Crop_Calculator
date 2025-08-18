#######################################################################################################################################
# Title: main
# Author: Tony Pescatore
# Description: Main will utilize functions from library.py and inputs from the user to generate the cost of planting all your crops.
#######################################################################################################################################

# Imports
import library as lib
from fertilizer import get_fertilizer_used
from crop import generate_crops, crop_auto_correct, get_crop_selection

def main():
    print('MAIN TETSER: ')
    tester = ' - 25 '
    try:

        tester = int(tester.strip())
        print('tester was turned into int!:', tester)
    except:
        print('error converting to int')

    # lib.welcome_mess()
    # lib.thank_you_mess()
    # test2 = lib.seeds_to_buy()
    # print('Test2:', test2)
    
    # test3 = get_fertilizer_used()
    # print('Name: {} - Price: {} - Recipe: {} - Amount Crafted: {}'.format(test3.name, test3.price, test3.recipe, test3.amt_per_craft) )

    test4 = generate_crops()

    print(test4['corn'].gpd)

    corrections = crop_auto_correct('corn',test4)
    for i in range(len(corrections)):
        print(str(i+1) + '. Name:', corrections[i].name, 'Price:', corrections[i].seed_price)


    test5 = get_crop_selection(test4)
    print('Test5 Crop:', test5.name)
    
main()