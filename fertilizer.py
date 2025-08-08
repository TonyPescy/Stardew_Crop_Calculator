#######################################################################################################################################
# Title: fertlizer
# Author: Tony Pescatore
# Description: fertilizer class to house important information about the crops.
#######################################################################################################################################

# Import
from sprinkler import TO_INT_FAIL

class Fertilizer:
    # initialize basic fertilizer information
    def __init__(self, name, price, recipe, amt_per_craft = 1):
        self.name = name
        self.price = price      # if price is 0 then it cannot be bought
        self.recipe = recipe    # lists within list: [ [item, quantity], [item2, quantity] ... ]
        self.amt_per_craft = amt_per_craft

# Creates all the variants of fertilizer with their stats and returns a list of the fertilizer objects
def generate_fertilizer():
    bas_fert = Fertilizer('Basic Fertilizer', 100, [['Sap', 2]])
    qual_fert = Fertilizer('Quality Fertilizer', 150, [['Sap', 4], ['Any Fish', 1]], 2)
    del_fert = Fertilizer('Deluxe Fertilizer', 0, [['Iridium Bar', 1], ['Sap', 40]], 5)
    bas_ret = Fertilizer('Basic Retaining Soil', 100, [['Stone', 2]])
    qual_ret = Fertilizer('Quality Retaining Soil', 150, [['Stone', 3], ['Clay', 1]], 2)
    del_ret = Fertilizer('Deluxe Retaining Soil', 0, [['Stone', 5], ['Fiber', 3], ['Clay', 1]])
    speed_gro = Fertilizer('Speed-Gro', 100, [['Pine Tar', 1], ['Moss', 5]], 5)
    del_gro = Fertilizer('Deluxe Speed-Gro', 150, [['Oak Resin', 1], ['Bone Fragment', 5]], 5 )
    hyp_gro = Fertilizer('Hyper Speed-Gro', 0, [['Radiactive Ore', 1], ['Bone Fragment', 3], ['Solar Essence', 1]])

    fert_list = [bas_fert, qual_fert, del_fert, bas_ret, qual_ret, del_ret, speed_gro, del_gro, hyp_gro]
    return fert_list

# Asks user to choose whatever fertilizer they will use on their field
def get_fertilizer_used():
    fert_list = generate_fertilizer()

    while True:
        print('0. No Fertilizer')
        for i in range(1, len(fert_list)+1):
            print('{}. {}'.format(i, fert_list[i-1].name))
            
        # Repeats request for fertilizer response until it gets a valid response
        try:
            fert_res = int(input('Please enter the number corresponding to fertilizer you wish to use in your field: ').strip())
            if fert_res < 0 or fert_res > (len(fert_list)+1):
                int(TO_INT_FAIL)
            break
        except:
            print('Invalid resposnse. Please enter a whole number from the range provided.')

    # returns fertilizer object that was selected
    selected_fert = fert_list[fert_res-1]
    return selected_fert