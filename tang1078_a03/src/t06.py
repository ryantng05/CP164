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
from functions import postfix

test_expressions = [
    "12 5 -",
    "4 5 + 12 * 2 3 * -",
    "7 2 + 3 /"
]

for expr in test_expressions:
    result = postfix(expr)
    print(f"'{expr}' evaluates to {result}")