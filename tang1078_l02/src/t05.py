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
from utilities import stack_test
from Food_utilities import read_foods

fh = open("foods.txt", 'r')

stack_test(read_foods(fh))