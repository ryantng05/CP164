"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Ryan Tang
ID:      169061078
Email:   tang1078@mylaurier.ca
__updated__ = "2024-02-16"
-------------------------------------------------------
"""
# Imports
from List_linked import List

my_list = List()
my_list.append(5)
my_list.append(4)
my_list.append(3)
my_list.append(2)

previous_node, current_node, index = my_list._linear_search(5)

print("Previous Node Value:", previous_node._value if previous_node else None)
print("Current Node Value:", current_node._value if current_node else None)
print("Index of Node with Value 5:", index)