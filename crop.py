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

# Creates all the variants of crops with their stats
# All gpd values are based on being planted and water from day 1 of their month
# all prices are based on Pierre's shop cuz who uses jojomart except for the achievement?
# Returns ordered list of crop objects
def generate_crops():
    # Initialize crop dictionary
    crop_dict = {}
    # Open crop.csv
    with open('Crop_And_Field_CSVs/crop.csv') as crop_csv_file:
        # Skip csv header 
        next(crop_csv_file)
        # Read file line by line
        for line in crop_csv_file:
            # assign columns from csv
            name, seed_price, season, profit_per_day = line.strip().split(',')
            # Ensure valid values from csv file
            try:
                seed_price = int(seed_price)
                profit_per_day = float(profit_per_day)
            except:
                print('Error reading crop csv file.')
                print(f'Error with crop: {name}!')

            # Create crop object
            temp_crop = Crop(name, seed_price, season, profit_per_day)
            # Add crop to crop dictionary
            key = name.lower().replace(' ', '')
            crop_dict[key] = temp_crop

    # Return filled crop dictionary
    return crop_dict

# Uses user-inputted crop name and checks to see if there are any spelling errors or if what was entered is a valid crop
# crop_name =  string inputted by user to be checked if it is in or similar to crops in our dictionary
# crop_dictionary = key:value dictionary of crop objects used to find users chosen crop
def crop_auto_correct(crop_name, crop_dictionary):
    # normalize to match your dict keys (lowercase, no spaces)
    key = ''.join(ch for ch in crop_name.lower() if ch.isalnum())
    n = len(key)
    letters = string.ascii_lowercase

    results = []
    seen = set()

    # 0-edit (exact match)
    if key in crop_dictionary:
        results.append(crop_dictionary[key])
        seen.add(key)

    # 1 substitution
    for i in range(n):
        orig_i = key[i]
        for c1 in letters:
            if c1 == orig_i:
                continue
            cand1 = key[:i] + c1 + key[i+1:]
            if cand1 in crop_dictionary and cand1 not in seen:
                results.append(crop_dictionary[cand1])
                seen.add(cand1)

    # 2 substitutions at any two positions
    for i in range(n):
        orig_i = key[i]
        for c1 in letters:
            if c1 == orig_i:
                continue
            s1 = key[:i] + c1 + key[i+1:]
            for j in range(i+1, n):
                orig_j = s1[j]
                for c2 in letters:
                    if c2 == orig_j:
                        continue
                    cand2 = s1[:j] + c2 + s1[j+1:]
                    if cand2 in crop_dictionary and cand2 not in seen:
                        results.append(crop_dictionary[cand2])
                        seen.add(cand2)

    return results


# Will get user inputted response for which crop they would like to plant in their fields
def get_crop_selection():
    crop_dictionary = generate_crops()
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
            crop_res = (input('Please enter the crop name you would like to plant: ').lower()).strip()
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
                                #print(corrections[corr_res-1])
                                return corrections[corr_res-1]
                    except:
                        print('Invalid response, please respond with a valid number within the given range.')

        except:
            print('Please respond with a valid crop name.')



# Displays crop suggestions based on season provided
# season = user entered season (string)
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