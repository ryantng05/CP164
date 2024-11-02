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
from Food_utilities import by_origin
from Food_utilities import read_foods

fh = open("foods.txt", 'r')

for food in by_origin(read_foods(fh), 1):
    print(food)