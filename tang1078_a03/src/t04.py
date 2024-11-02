"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Ryan Tang
ID:      169061078
Email:   tang1078@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

source = Stack()
list1 = [8, 12, 8, 5]

for i in list1:
    source.push(i)

source.reverse()

for j in source:
    print(j)