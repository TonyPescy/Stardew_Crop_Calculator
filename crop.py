#######################################################################################################################################
# Title: crop
# Author: Tony Pescatore
# Description: crop class to house important information about the crops.
#######################################################################################################################################


class Crop:
    # initialize basic crop information
    def __init__(self, name, seed_price, season):
        self.name = name
        self.seed_price = seed_price
        self.season = season

    