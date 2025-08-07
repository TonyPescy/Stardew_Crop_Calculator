#######################################################################################################################################
# Title: library
# Author: Tony Pescatore
# Description: Library will provide functions that will be called in main.py
#######################################################################################################################################

# Imports
from crop import Crop

# Constants
TO_INT_FAIL = 'F'

# Welcome message for start of calc
def welcome_mess():
    print('Hello, welcome to the Stardew Valley Crop Calculator! This tool will help you determine how much it will cost for you to fully plant and fertilize your farm.')

# 
def display_info():
    print('NAN')

# Thanks user for using calc
def thank_you_mess():
    print('Thank you for using my Stardew Valley Crop Calculator!')


def seeds_to_buy():
    # seeds_needed = 0
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
            while True:
                # Repeats request for standard sprinkler number until valid answer
                try:
                    spr = int(input('How many standard sprinklers do you have? (Please answer with a whole number as such: 5): ').strip())
                    if spr < 0:
                        int(TO_INT_FAIL)
                    break
                except:
                    print('Invalid resposnse. Please enter a whole number equal to or greater than 0.')

            while True:
                # Repeats request for quality sprinkler number until valid answer
                try:
                    qual_spr = int(input('How many quality sprinklers do you have? (Please answer with a whole number as such: 5): ').strip())
                    if qual_spr < 0:
                        int(TO_INT_FAIL)
                    break
                except:
                    print('Invalid resposnse. Please enter a whole number equal to or greater than 0.')

            while True:
                # Repeats request for iridium sprinkler number until valid answer
                try:
                    iri_spr = int(input('How many iridium sprinklers do you have? (Please answer with a whole number as such: 5): ').strip())
                    if iri_spr < 0:
                        int(TO_INT_FAIL)
                    break
                except:
                    print('Invalid resposnse. Please enter a whole number equal to or greater than 0.')

            print('NAN')
            

        else:
            # Invalid respone for known_seeds_res
            print('Invalid response, please enter "Yes" or "no".')
    
    # Returns valid number of seeds needed for next section of calc
    return int(seeds_needed)