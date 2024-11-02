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
from Food_utilities import write_foods
from Food import Food

file_variable = open("new_foods.txt", 'w')

foods = [Food("Rice", 3, True, 90), Food("Sugar", 1, False, 1)]

write_foods(file_variable, foods)

file_variable.close()