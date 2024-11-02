"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Ryan Tang
ID:      169061078
Email:   tang1078@mylaurier.ca
__updated__ = "2024-02-24"
-------------------------------------------------------
"""
# Imports
from List_array import List

list = List()
list2 = List()

list.append(0)
list.append(0)
list.append(0)


target1, target2 = list.split_alt()

for val in target1:
    print(val)
