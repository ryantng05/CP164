"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Ryan Tang
ID:      169061078
Email:   tang1078@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods

file_variable = open("foods.txt", 'r')

for food in read_foods(file_variable):
    print(food)