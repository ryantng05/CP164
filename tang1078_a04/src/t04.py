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
from Queue_array import Queue

source_queue = Queue()
# Fill the source queue with some values
for i in range(10):
    source_queue.insert(i)

# Split the source queue into two alternating queues
target1, target2 = source_queue.split_alt()

# Display the resulting queues
print("Target 1 Queue:")
for value in target1:
    print(value, end=' ')
print()

print("Target 2 Queue:")
for value in target2:
    print(value, end=' ')
print()