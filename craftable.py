#######################################################################################################################################
# Title: craftable
# Author: Tony Pescatore
# Description: craftable class to house important information about the craftable items
#######################################################################################################################################

# Constant
CRAFTABLE_TYPES = ['Artisan Equipment', 'Bombs', 'Decor', 'Fences', 'Fishing Items', 'Rings', 'Seeds', 'Sprinklers']   # contains 

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

# Asks user what item they would like to craft from their selected type
# Returns item to be crafted object
def get_craftable_item():
    # Repeats until an item is found for the user
    while True:
        # Get craftable type
        craftable_type = get_crafting_type()
        # Get list of items from craftable type
        craftable_type_item_list = read_recipe_csv(craftable_type)
        # List all options to user until proper response is given
        while True:
            for i in range(1, len(craftable_type_item_list)):      # Exclude tree fertilizer (i=10) as that would not be used on a seeded field
                print('{}. {}'.format(i, craftable_type_item_list[i-1].name))
                
            # Repeats request for item choice until it gets a valid response
            try:
                item_res = int(input('Please enter the number corresponding to item you wish to craft (If your desired item is not present enter 0 and try another craftable type): ').strip())
                if item_res < 0 or item_res > (len(craftable_type_item_list)+1):
                    int(TO_INT_FAIL)
                break
            except:
                print('Invalid resposnse. Please enter a whole number from the range provided.')
        
        # Ensures user finds their craftable item
        if item_res != 0:
            # Get quantity for item selected
            while True:
                try:
                    item_quantity = int(input(f'Please enter the number of {craftable_type_item_list[item_res]}s you would like to craft: ').strip())
                    # Checks for valid response
                    if item_quantity <= 0:
                        int(TO_INT_FAIL)
                    break
                except:
                    print('Invalid resposnse. Please enter a whole number above 0')
            # Exit first while true loop      
            break
    # Create tuple for returning
    item_quantity_tuple = (craftable_type_item_list[item_res], item_quantity)
    # Return item object from response
    return item_quantity_tuple

# Gets all craftable items user wants to craft
#
def crafting_calculator():
    # Initlize list of users tuples (items, quantity) to craft
    items_to_craft = []
    while True:
        # Get user item and the amount they would like to craft
        items_to_craft.append(get_craftable_item())

        while True:
            try:
                try_again_res = (input('Now that you have found an item would you like to add another item? Please enter yes or no: ').lower()).strip()
                if try_again_res == 'yes' or try_again_res == 'no':
                    break
                else:
                    int(TO_INT_FAIL)
            except:
                print('Invalid response, please respond with yes or no.')
        
        if try_again_res == 'no':
            break
        # Else - Repeat while true loop
    # Display user recipes
    print('Here is what you would need to craft you selected item(s):')
    for i in range(1, len(items_to_craft)+1):
        print('{}. {} ')
        
