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
from Food_utilities import food_table
from Food_utilities import read_foods

fh = open("foods.txt", 'r')

food_table(read_foods(fh))
