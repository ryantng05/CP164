"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Ryan Tang
ID:      169061078
Email:   tang1078@mylaurier.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
# Imports
from Food_utilities import food_search
from Food_utilities import read_foods

fh = open("foods.txt", 'r')
origin = 1
max_cals = 200
is_veg = False

for food in food_search(read_foods(fh), origin, max_cals, is_veg):
    print(food)