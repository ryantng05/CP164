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
my_list.append("apple")
my_list.append("banana")
my_list.append("cherry")
my_list.append("date")

found_item = my_list.find("banana")
print("Found item:", found_item)

index_of_cherry = my_list.index("cherry")
print("Index of 'cherry':", index_of_cherry)

contains_apple = "apple" in my_list
print("Is 'apple' in the list?", contains_apple)