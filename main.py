#######################################################################################################################################
# Title: main
# Author: Tony Pescatore
# Description: Main will utilize functions from library.py and inputs from the user to generate the cost of planting all your crops.
#######################################################################################################################################

# Imports
import library as lib

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
    test2 = lib.seeds_to_buy()
    print('Test2:', test2)

main()