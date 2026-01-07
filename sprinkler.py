#######################################################################################################################################
# Title: sprinkler
# Author: Tony Pescatore
# Description: sprinkler class to house important information about the sprinklers.
#######################################################################################################################################

# import
from library import TO_INT_FAIL

class Sprinkler:
    # initialize sprinklers information
    def __init__(self, name, tiles_watered, tiles_with_nozzle):
        self.name = name
        self.tiles_watered = tiles_watered
        self.tiles_with_nozzle = tiles_with_nozzle

# Reads and creates the three variants of sprinklers with their stats
# Returns list of Sprinkler objects
def generate_sprinklers():
    # Initialize empty list for sprinklers
    sprinkler_list = []

    # Open sprinkler.csv 
    with open('Crop_And_Field_CSVs/sprinkler_stats.csv') as sprinkler_csv_file:
        # Skip csv header
        next(sprinkler_csv_file)
        # Read file line by line
        for line in sprinkler_csv_file:
            # Assign columns from csv
            name, watered, with_nozzle = line.strip().split(',')
            # Ensure valid values from csv file
            try:
                watered = int(watered)
                with_nozzle = int(with_nozzle)
            except:
                print('Error reading sprinkler csv file.')
                print(f'Error with sprinkler: {name}!')

            # Create sprinkler object and append to list
            sprinkler_list.append(Sprinkler(name, watered, with_nozzle))

    return sprinkler_list

# Will ask user to input how mnay sprinklers of each type they have
def get_number_of_sprinklers():
    while True:
        # Repeats request for standard sprinkler number until valid answer
        try:
            spr = int(input('How many standard sprinklers do you have? (Please answer with a whole number): ').strip())
            if spr < 0:
                int(TO_INT_FAIL)
            break
        except:
            print('Invalid resposnse. Please enter a whole number equal to or greater than 0.')

    while True:
        # Repeats request for quality sprinkler number until valid answer
        try:
            qual_spr = int(input('How many quality sprinklers do you have? (Please answer with a whole number): ').strip())
            if qual_spr < 0:
                int(TO_INT_FAIL)
            break
        except:
            print('Invalid resposnse. Please enter a whole number equal to or greater than 0.')

    while True:
        # Repeats request for iridium sprinkler number until valid answer
        try:
            iri_spr = int(input('How many iridium sprinklers do you have? (Please answer with a whole number): ').strip())
            if iri_spr < 0:
                int(TO_INT_FAIL)
            break
        except:
            print('Invalid resposnse. Please enter a whole number equal to or greater than 0.')

    num_of_spr_list = [spr, qual_spr, iri_spr]
    return num_of_spr_list

# Will ask user for how pressure nozzles they have
def get_number_of_nozzles():
    while True:
        # Repeats request for pressure nozzles number until valid answer
        try:
            p_noz = int(input('How many pressure nozzles do you have? (Please answer with a whole number and if you have no nozzles, respond with 0.): ').strip())
            if p_noz < 0:
                int(TO_INT_FAIL)
            break
        except:
            print('Invalid resposnse. Please enter a whole number and if you have no nozzles enter 0.')
    return p_noz

# Asks user how many watered tiles will be unavailable for crops to be planted
def get_number_of_blocked_tiles():
    while True:
        # Repeats request for unusable watered tiles number until valid answer
        try:
            print('Common unusable tiles include: Scarecrows, rocks/boulders, trees/stumps, fences, etc.')
            unusable_tiles = int(input('How many unusable tiles do you have? (Please answer with a whole number and if you have no unusable tiles, please respond with 0.): ').strip())
            if unusable_tiles < 0:
                int(TO_INT_FAIL)
            break
        except:
            print('Invalid resposnse. Please enter a whole number and if you have no unusable tiles enter 0.')
    return unusable_tiles

# Using functions from sprinkler.py this will determine how many seeds the user will need to plant their whole field
def seeds_to_buy():
    seeds_needed = 0
    known_seeds_res = ''
    valid_res = False
    while known_seeds_res != 'yes' and known_seeds_res != 'no':
        known_seeds_res = (input('Do you know how many seeds you need for your entire field? Please respond with Yes or No: ').lower()).strip()

        if known_seeds_res == 'yes':
            # Asks for user value of seeds until it gets a valid integer from user
            while valid_res == False:
                seeds_needed = input('Please enter the number of seeds you need to buy: ')
                try:
                    if int(seeds_needed) <= 0:
                        print('Please enter a number larger than 0 to proceed.')
                    else:   # Only way to exit while - Valid entry provided by user
                        #print('Valid User input!')
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
                seeds_needed -= blocked_tiles
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
                seeds_needed -= blocked_tiles
                if press_noz > 0:
                    print('You have ' + str(press_noz) + ' pressure nozzle(s) left. You should craft more sprinklers if you are able to!')
        else:
            # Invalid respone for known_seeds_res
            print('Invalid response, please enter yes or no.')
            
    
    return int(seeds_needed)