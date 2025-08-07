#######################################################################################################################################
# Title: sprinkler
# Author: Tony Pescatore
# Description: sprinkler class to house important information about the sprinklers.
#######################################################################################################################################

class Sprinkler:
    # initialize basic crop information
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