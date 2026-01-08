#######################################################################################################################################
# Title: cooking
# Author: Tony Pescatore
# Description: cooking class to house important information about the food and cooking recipes.
#######################################################################################################################################

# Imports
from library import TO_INT_FAIL
from craftable import Craftable     # Parent class imported for Fertilizer child class

# Cooking extends craftable class and inherits its name, recipe, recipe_source, amt_per_craft
# It adds new parameters: sell_price, health, energy, buff, and buff_duration
class Cooking(Craftable):
    # initialize basic fertilizer information
    def __init__(self, name, recipe, recipe_source, amt_per_craft, sell_price, health, energy, buff = ['None'], buff_duration = 'None' ):
        Craftable.__init__(self, name, recipe, recipe_source, amt_per_craft)    # Inherit from craftable class
        self.sell_price = sell_price  # New variable sell_price
        self.health = health  # New variable health
        self.energy = energy  # New variable energy
        self.buff = buff  # New variable buff - Default = 'NONE'
        self.buff_duration = buff_duration  # New variable buff_duration - Default = 'NONE'
    
# Reads cooking CSV
# Returns list of all cooking objects
def read_cooking_csv():
    # Initialize list of cooking objects
    cooking_item_list = []
    # Open cooking recipe csv
    with open(f'Cooking_CSVs/recipes.csv') as recipe_csv_file:
        # Skip csv header
        next(recipe_csv_file)
        # Read file line by line
        for line in recipe_csv_file:
            # Assign columns from csv
            name, recipe, recipe_source, amt_per_craft, sell_price, health, energy, buff, buff_duration = line.strip().split(',')
    
            # Create recipe from csv
            # Initialize recipe list
            recipe_list = []
            for ingredient in recipe.split(';'):
                ingredient_name, quantity = ingredient.split(':')
                # Adds ingredient to recipe list
                recipe_list.append([ingredient_name, quantity])
            
            # Create buff list from csv
            # Initialize buff list
            buff_list = []
            for power in buff.split(';'):
                # Adds buff to recipe list
                buff_list.append([power])
            
            # Checks for buffs
            if buff != '':     # If item has buffs
                # Create craftable item object
                temp_cooking_item = Cooking(name, recipe_list, recipe_source, amt_per_craft, sell_price, health, energy, buff_list, buff_duration)

            else:       # If there is no buff
                temp_cooking_item = Cooking(name, recipe_list, recipe_source, amt_per_craft, sell_price, health, energy)
            
            # Add cooking item object to the cooking item list
            cooking_item_list.append(temp_cooking_item)

    # Returns completed list of cooking objects
    return cooking_item_list

# Asks user what item they would like to cook from all possible options
# Returns tuple of item to be cooked
def get_cooking_item():
    # Repeats until an item is found for the user
    while True:
        # Read Cooking csv
        cooking_item_list = read_cooking_csv()
        while True:
            for i in range(1, len(cooking_item_list)+1):      
                print('{}. {}'.format(i, cooking_item_list[i-1].name))
                
            # Repeats request for item choice until it gets a valid response
            try:
                item_res = int(input('Please enter the number corresponding to dish you wish to cook: ').strip())
                if item_res < 0 or item_res > (len(cooking_item_list)):
                    int(TO_INT_FAIL)
                break
            except:
                print('Invalid resposnse. Please enter a whole number from the range provided.\n')
        
        # Ensures user finds their cooking item
        if item_res != 0 and item_res <= (len(cooking_item_list)+1):
            # Get quantity for item selected
            while True:
                try:
                    item_quantity = int(input(f'Please enter the number of {cooking_item_list[item_res-1].name}s you would like to cook: ').strip())
                    # Checks for valid response
                    if item_quantity <= 0:
                        int(TO_INT_FAIL)
                    break
                except:
                    print('Invalid resposnse. Please enter a whole number above 0')
            # Exit first while true loop      
            break
    # Create tuple for returning
    item_quantity_tuple = (cooking_item_list[item_res-1], item_quantity)
    # Return item object from response
    return item_quantity_tuple

def cooking_calculator():
    # Initlize list of users tuples (items, quantity) to cook
    items_to_cook = []
    while True:
        # Get user dish(s) and the amount they would like to cook
        items_to_cook.append(get_cooking_item())

        while True:
            try:
                try_again_res = (input('Now that you have found a dish would you like to add another dish? Please enter yes or no: ').lower()).strip()
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
    if len(items_to_cook) == 1:
        print('\nHere is what you would need to cook your selected dish:')
    else:
        print('\nHere is what you would need to cook your selected dishes:')
        
    for i in range(1, len(items_to_cook)+1):
        # Print list number, name of item, and item quantity
        print('{}. {} x{}'.format(i, items_to_cook[i-1][0].name, items_to_cook[i-1][1])) # i-Number, items_to_cook[i-1][0]-Object, items_to_cook[i-1][1]-Quantity
        temp_recipe_source = items_to_cook[i-1][0].recipe_source   # String containing recipe source

        print('\tRequired Ingredients:')
        # Print recipe item by item
        for recipe_item in items_to_cook[i-1][0].recipe:
            print('\t\t{} x{}'.format(recipe_item[0], str((int(recipe_item[1]) * int(items_to_cook[i-1][1])))))  # recipe_item[0]-Item name, recipe_item[1]-Number of items required, items_to_cook[i-1][1]-Quantity of cooks to be done
        
        # Print Buffs or lack thereof
        print('\tBuff(s):')
        for buff in items_to_cook[i-1][0].buff:
            # If buff has multiple benefits/powers
            if isinstance(buff, list):      
                print('\t\t{}'.format(', '.join(buff)))
            else:
                print('\t\t{}'.format(buff))
        # Print buff duration
        print('\tBuff Duration:')
        print('\t\t{}'.format(items_to_cook[i-1][0].buff_duration))

        # Print source of recipe
        if temp_recipe_source == 'Starter':
            print('\tYou start the game with this recipe!')
        else:
            temp_recipe_source = temp_recipe_source[0].lower() + temp_recipe_source[1:] # Sentence format fix
            print('\tYou receive this recipe by {}!'.format(temp_recipe_source))