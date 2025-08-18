#######################################################################################################################################
# Title: crop
# Author: Tony Pescatore
# Description: crop class to house important information about the crops.
#######################################################################################################################################

# imports
import string
from library import TO_INT_FAIL

class Crop:
    # initialize basic crop information
    def __init__(self, name, seed_price, season, gpd):
        self.name = name
        self.seed_price = seed_price
        self.season = season
        self.gpd = gpd

# Creates all the variants of crops with their stats and returns a list of the ordered crop objects
# All gpd values are based on being planted and water from day 1 of their month
# all prices are based on Pierre's shop cuz who uses jojomart except for the achievement?
def generate_crops():
    bl_jz = Crop('Blue Jazz', 30, 'Spring', 2.86)
    cauli = Crop('Cauliflower', 80, 'Spring', 7.92)
    garlic = Crop('Garlic', 40, 'Spring', 5)
    grn_bn = Crop('Green Bean', 60, 'Spring', 7.2)
    kale = Crop('Kale', 70, 'Spring', 6.67)
    prsnp = Crop('Parsnip', 20, 'Spring', 3.75)
    pot = Crop('Potato', 50, 'Spring', 8.33)
    rhub = Crop('Rhubarb', 100, 'Spring', 9.23)
    stwbry = Crop('Strawberry', 100, 'Spring', 20.83)
    tul = Crop('Tulip', 20, 'Spring', 1.67)
    rice = Crop('Unmilled Rice', 40, 'Spring', -1.67)

    blbry = Crop('Blueberry', 80, 'Summer', 20.8)
    corn_s = Crop('Corn', 150, 'Summer', 7.41)
    hops = Crop('Hops', 60, 'Summer', 13.52)
    hot_pep = Crop('Hot Pepper', 40, 'Summer', 10.77)
    melon = Crop('Melon', 80, 'Summer', 14.17)
    pop = Crop('Poppy', 100, 'Summer', 5.71)
    rad = Crop('Radish', 40, 'Summer', 8.33)
    rd_cab = Crop('Red Cabbage', 100, 'Summer', 17.78)
    strfrt = Crop('Starfruit', 400, 'Summer', 26.92)
    sum_spngl = Crop('Summer Spangle', 50, 'Summer', 5)
    snflwr_s = Crop('Sunflower', 200, 'Summer', -15)
    tom = Crop('Tomato', 50, 'Summer', 9.26)
    wht_s = Crop('Wheat', 10, 'Summer', 3.75)

    ama = Crop('Amaranth', 70, 'Fall', 11.43)
    arti = Crop('Artichoke', 30, 'Fall', 16.25)
    beet = Crop('Beet', 20, 'Fall', 13.33)
    bok = Crop('Bok Choy', 50, 'Fall', 7.5)
    #corn_f = Crop('Corn', 150, 'Fall', 1.92)
    cranbry = Crop('Cranberries', 240, 'Fall', 18.89)
    egplnt = Crop('Eggplant', 20, 'Fall', 11.2)
    fry_rs = Crop('Fairy Rose', 200, 'Fall', 7.5)
    grp = Crop('Grape', 60, 'Fall', 16.8)
    pmpkn = Crop('Pumpkin', 100, 'Fall', 16.92)
    #snflwr_f = Crop('Sunflower', 200, 'Fall', -30)
    #wht_f = Crop('Wheat', 10, 'Fall', 1.875)
    yam = Crop('Yam', 60, 'Fall', 10)

    # Crop dictionary creation
    crop_dict = {
        value.name.lower().replace(" ", ""): value
        for value in locals().values()
        if isinstance(value, Crop)
    }

    return crop_dict

# Uses user-inputted crop name and checks to see if there are any spelling errors or if what was entered is a valid crop
def crop_auto_correct(crop_name, crop_dictionary):
    possible_corrections = []
    name_len = len(crop_name)

    for i in range(name_len):   # used to iterates over every letter in crop name
        temp_name = crop_name   # resets temp_word

        for letter1 in string.ascii_lowercase:      # changes 1 letter in crop name
            temp_name = temp_name[:i] + letter1 + temp_name[i+1:]
            if crop_dictionary.get(temp_name) != None and crop_dictionary.get(temp_name) not in possible_corrections:    # if not None then word is found
                possible_corrections.append(crop_dictionary.get(temp_name)) # Adds crop object to possible corrections
            
            if (i+1) < name_len:
                for letter2 in string.ascii_lowercase:  # changes a second letter in crop name
                    temp_name = temp_name[:i+1] + letter2 + temp_name[i+2:]
                    if crop_dictionary.get(temp_name) != None and crop_dictionary.get(temp_name) not in possible_corrections:    # if not None then word is found
                        possible_corrections.append(crop_dictionary.get(temp_name)) # Adds crop object to possible corrections
    
    return possible_corrections


# Will get user inputted response for which crop they would like to plant in their fields
def get_crop_selection(crop_dictionary):
    while True:
        try:
            sugg_res = (input('Now that we know the size of your field, now we need to know what you would like to plant. Would you like suggestions? Please enter yes or no: ').lower()).strip()
            if sugg_res == 'yes' or sugg_res == 'no':
                break
            else:
                int(TO_INT_FAIL)
        except:
            print('Invalid response, please respond with yes or no.')

    if sugg_res == 'yes':
        while True:
            try:
                seas_res = (input('Please enter the season (Spring, Summer, or Fall) that you are planting in: ').lower()).strip()
                if seas_res == 'spring' or seas_res == 'summer' or seas_res == 'fall':
                    crop_suggestions(seas_res)
                    break
                else:
                    int(TO_INT_FAIL)
            except:
                print('Invalid response, please respond with Spring, Summer, or Fall.')

    while True:
        try:
            crop_res = (input('Please enter the crop you would like to plant: ').lower()).strip()
            if  crop_dictionary.get(crop_res) != None:      # valid crop name entered
                return crop_dictionary.get(crop_res)
            
            else:
                corrections = crop_auto_correct(crop_res, crop_dictionary)

                if len(corrections) == 0:
                    print('We found no similar crop matches, please try again!')
                    int(TO_INT_FAIL)

                print('Did you mean:')
                for i in range(len(corrections)):
                    print(str(i+1) + '.', corrections[i].name)

                while True:
                    try:
                        corr_res = int(input('Please enter the number corresponding to the crop want to plant. If the crop you want is not on this list, please enter 0: ').strip())
                        if corr_res <= len(corrections) and corr_res >= 0:   # valid int response
                            if corr_res == 0:
                                print('Sorry for the failure to find a matching crop, please try again.')
                                break
                            else:
                                print(corrections[corr_res-1])
                                return corrections[corr_res-1]
                    except:
                        print('Invalid response, please respond with a valid number within the given range.')

        except:
            print('Please respond with a valid crop name.')



# Displays crop suggestions based on season provided
def crop_suggestions(season):
    match season:
        case 'spring':
            print('1. Strawberry - Best overall spring crop.')
            print('2. Rhubarb - Second best spring crop.')
            print('3. Potato - Third best spring crop.')
            print('4. Strawberry - Best spring crop for artisan goods.')
        case 'summer':
            print('1. Starfruit - Best overall summer crop.')
            print('2. Blueberry - Second best summer crop.')
            print('3. Red Cabbage - Third best summer crop.')
            print('4. Starfruit - Best summer crop for jarring.')
            print('5. Hops - Best summer crop for kegs, especially when aged with casks.')
        case 'fall':
            print('1. Cranberries - Best overall fall crop.')
            print('2. Pumpkin - Second best fall crop.')
            print('3. Grape - Third best fall crop')
            print('4. Cranberries - Best crop for artisan goods.')