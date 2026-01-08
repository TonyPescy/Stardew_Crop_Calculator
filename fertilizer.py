#######################################################################################################################################
# Title: fertlizer
# Author: Tony Pescatore
# Description: fertilizer class to house important information about the fertilizers.
#######################################################################################################################################

# Imports
from library import TO_INT_FAIL
from craftable import Craftable     # Parent class imported for Fertilizer child class

# Fertilizer extends craftable class and inherits its name, recipe, recipe_source, amt_per_craft
# It adds a new parameter price
class Fertilizer(Craftable):
    # initialize basic fertilizer information
    def __init__(self, name, price, recipe, recipe_source, amt_per_craft = 1):
        Craftable.__init__(self, name, recipe, recipe_source, amt_per_craft)    # Inherit from craftable class
        self.price = price  # New variable price

# Creates all the variants of fertilizer with their stats and returns a list of the fertilizer objects
# Returns list of Fertilizer objects
def generate_fertilizer():
    # Initialize fertilizer list
    fertilizer_list = []
    # Open fertilizer.csv
    with open('Crop_And_Field_CSVs/fertilizer.csv') as fertilizer_file:
        # Skip csv header
        next(fertilizer_file)
        # Read file line by line
        for line in fertilizer_file:
            # Assign columns from csv - recipe_source is not used in crop field calculations
            name, price, recipe, recipe_source, amt_per_craft = line.strip().split(",")
            
            # Create recipe from csv
            # Initialize recipe list
            recipe_list = []
            for ingredient in recipe.split(';'):
                ingredient_name, quantity = ingredient.split(':')
                
                # Ensure valid values for quantity
                try:
                    quantity = int(quantity)
                except:
                    print('Error reading recipe from fertilizer csv file.')
                    print(f'Error with recipe: {name} and ingredient {ingredient_name}!')
                
                # Add seperated ingredients to the recipe list
                recipe_list.append([ingredient_name, quantity])
            
            # Create fertilizer object
            if amt_per_craft != '':     # If amount per craft is specified
                # Ensure valid values from csv file
                try:
                    amt_per_craft = int(amt_per_craft)
                    price = int(price)
                except:
                    print('Error reading fertilizer csv file.')
                    print(f'Error with price and/or amount per craft from: {name}!')

                temp_fertilizer = Fertilizer(name, price, recipe_list, recipe_source, amt_per_craft)

            else:       # amt_per_craft not specified
                # Ensure valid values for price
                try:
                    price = int(price)
                except:
                    print('Error reading fertilizer csv file.')
                    print(f'Error with price from: {name}!')

                temp_fertilizer = Fertilizer(name, price, recipe_list, recipe_source)
            
            # Add fertilizer object to the fertilizer list
            fertilizer_list.append(temp_fertilizer)

    return fertilizer_list

# Asks user to choose whatever fertilizer they will use on their field
def get_fertilizer_used():
    fert_list = generate_fertilizer()

    while True:
        print('0. No Fertilizer')
        for i in range(1, len(fert_list)):      # Exclude tree fertilizer (i=10) as that would not be used on a seeded field
            print('{}. {}'.format(i, fert_list[i-1].name))
            
        # Repeats request for fertilizer response until it gets a valid response
        try:
            fert_res = int(input('Please enter the number corresponding to the fertilizer you wish to use in your field: ').strip())
            if fert_res < 0 or fert_res > (len(fert_list)+1):
                int(TO_INT_FAIL)
            break
        except:
            print('Invalid resposnse. Please enter a whole number from the range provided.')

    # returns fertilizer object that was selected
    if fert_res == 0:
        selected_fert = fert_list[fert_res] 
    else:   # Prevents 0 from becoming -1 (last option)
        selected_fert = fert_list[fert_res-1]
    return selected_fert