"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Ryan Tang
ID:      169061078
Email:   tang1078@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List

original_list = List()
for value in range(1, 6):  # This will create a list with values 1 to 5
    original_list.append(value)

# Display the original list order.
print("Original List:")
current = original_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()

# Reverse the list using the recursive method.
original_list.reverse_r()

# Display the reversed list order.
print("Reversed List:")
current = original_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()