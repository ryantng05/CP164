"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Ryan Tang
ID:      169061078
Email:   tang1078@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack

s = Stack()

source = [99]

array_to_stack(s, source)

for i in s:
    print(i)

