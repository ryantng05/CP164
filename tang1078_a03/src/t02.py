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

source1 = Stack()
source2 = Stack()

list1 = [8, 12, 8, 5]
list2 = [14, 9, 7, 1, 6, 3]

for i in list1:
    source1.push(i)
for j in list2:
    source2.push(j)

target = Stack()

target.combine(source1, source2)

for i in target:
    print(i)