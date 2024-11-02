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
my_list.append(100)
my_list.append(90)
my_list.append(80)
my_list.append(70)
my_list.append(60)

count_20 = my_list.count(20)
print("The value '20' appears", count_20, "times in the list.")

max_value = my_list.max()
print("The maximum value in the list is:", max_value)

min_value = my_list.min()
print("The minimum value in the list is:", min_value)