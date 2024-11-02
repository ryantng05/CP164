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
from Stack_array import Stack
from utilities import stack_to_array, array_to_stack
# Constants

s = Stack()

source = [10,99,0,3,4]

target = []

array_to_stack(s, source)

stack_to_array(s, target)

print(target)