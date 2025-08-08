#######################################################################################################################################
# Title: sprinkler
# Author: Tony Pescatore
# Description: sprinkler class to house important information about the sprinklers.
#######################################################################################################################################

# Imports
TO_INT_FAIL = 'F'

class Sprinkler:
    # initialize sprinklers information
    def __init__(self, name, tiles_watered, tiles_with_nozzle):
        self.name = name
        self.tiles_watered = tiles_watered
        self.tiles_with_nozzle = tiles_with_nozzle

# Creates the three variants of sprinklers with their stats and returns a list of the Sprinkler objects
def generate_sprinklers():
    basic_spr = Sprinkler('Sprinkler', 4, 8)
    qual_spr = Sprinkler('Quality Sprinkler', 8, 24)
    iri_spr = Sprinkler('Iridium Sprinkler', 24, 48)

    sprinkler_list = [basic_spr, qual_spr, iri_spr]
    return sprinkler_list

# Will ask user to input how mnay sprinklers of each type they have
def get_number_of_sprinklers():
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

    num_of_spr_list = [spr, qual_spr, iri_spr]
    return num_of_spr_list

# Will ask user for how pressure nozzles they have
def get_number_of_nozzles():
    while True:
        # Repeats request for pressure nozzles number until valid answer
        try:
            p_noz = int(input('How many pressure nozzles do you have? (Please answer with a whole number as such 5 and if you have no nozzles, respond with 0.): ').strip())
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
            unusable_tiles = int(input('How many unusable tiles do you have? (Please answer with a whole number as such 5 and if you have no unusable tiles, respond with 0.): ').strip())
            if unusable_tiles < 0:
                int(TO_INT_FAIL)
            break
        except:
            print('Invalid resposnse. Please enter a whole number and if you have no unusable tiles enter 0.')
    return unusable_tiles