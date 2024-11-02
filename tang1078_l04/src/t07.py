"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Ryan Tang
ID:      169061078
Email:   tang1078@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from utilities import list_test
from List_array import List

llist = List()

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

for each in foods:
    llist.append(each)
    
list_test(llist)