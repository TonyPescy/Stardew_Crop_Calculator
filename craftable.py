#######################################################################################################################################
# Title: craftable
# Author: Tony Pescatore
# Description: craftable class to house important information about the craftable items
#######################################################################################################################################

# Constant
CRAFTABLE_TYPES = ['Artisan Equipment', 'Bombs', 'Decor', 'Fences', 'Seeds', 'Sprinklers']   # contains 

# Import
from library import TO_INT_FAIL

class Craftable:
    # Initialize basic craftable item info
    def __init__(self, name, recipe, recipe_source, amt_per_craft = 1):
        self.name = name
        self.recipe = recipe    # lists within list: [ [item, quantity], [item2, quantity] ... ]
        self.recipe_source = recipe_source
        self.amt_per_craft = amt_per_craft  # default = 1

# Open CSVs from Recipe_CSVs folder
# All files use the same exact format so use a universal opening function
# craftable_type = code word string that was selected by user and determines which type of item they want to craft (name of csv file)
# N0TE: craftable_type can never be fertilizer because the csv used has an extra column which is parsed with its own
#       specialized function. This should be checked and handled seperately from this universal recipe reader.
# Returns list of Craftable objects
def read_recipe_csv(craftable_type):
    # Initialize list of craftable items
    craftable_item_list = []
    # Open chosen craftable_type csv
    with open(f'Craftable_CSVs/{craftable_type.replace(" ", "_").lower()}.csv') as recipe_csv_file:
        # Skip csv header
        next(recipe_csv_file)
        # Read file line by line
        for line in recipe_csv_file:
            # Assign columns from csv
            name, recipe, recipe_source, amt_per_craft = line.strip().split(',')
    
            # Create recipe from csv
            # Initialize recipe list
            recipe_list = []
            for ingredient in recipe.split(';'):
                ingredient_name, quantity = ingredient.split(':')
                
                # Ensure valid values for quantity
                try:
                    quantity = int(quantity)
                except:
                    print(f'Error reading recipe from {craftable_type} csv file.')
                    print(f'Error with recipe: {name} and ingredient {ingredient_name}!')

                # Add seperated ingredients to the recipe list
                recipe_list.append([ingredient_name, quantity])
            
            # Ensures valid value for optional amt_per_craft
            if amt_per_craft != '':     # If amount per craft is specified
                # Ensure valid values from csv file
                try:
                    amt_per_craft = int(amt_per_craft)
                except:
                    print(f'Error reading {craftable_type} csv file.')
                    print(f'Error with amount per craft from: {name}!')
                # Create craftable item object
                temp_craftable = Craftable(name, recipe_list, recipe_source, amt_per_craft)

            else:       # If amount per craft is not specified in csv
                temp_craftable = Craftable(name, recipe_list, recipe_source)
            
            # Add craftable item object to the craftable item list
            craftable_item_list.append(temp_craftable)

    # Returns completed list of objects for selected craftable type
    return craftable_item_list

# Asks user to choose what type of crafting they want to be calculated
# Returns string that represents the users type of crafting to be done
def get_crafting_type():

    while True:
        print('From the following options please pick which craftables you would like to see:')
        for i in range(1, len(CRAFTABLE_TYPES)+1):     
            print('{}. {}'.format(i, CRAFTABLE_TYPES[i-1]))
            
        # Repeats request for craftable type response until it gets a valid response
        try:
            craftable_type_res = int(input('Please enter the number corresponding to craftable type you wish to see: ').strip())
            if craftable_type_res <= 0 or craftable_type_res >= (len(CRAFTABLE_TYPES)+1):
                int(TO_INT_FAIL)
            break
        except:
            print('Invalid resposnse. Please enter a whole number from the range provided.')

    return CRAFTABLE_TYPES[craftable_type_res]