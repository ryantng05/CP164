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
from List_array import List
from utilities import list_to_array
from utilities import array_to_list

# Create a List instance
llist = List()

source = [1, 2, 3, 4, 5]

array_to_list(llist, source)
print("List after array_to_list:")
for value in llist:
    print(value, end=' ')
print()

target = []
list_to_array(llist, target)
print("Python list after list_to_array:", target)
print("List is empty after transfer:", llist.is_empty())