"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Ryan Tang
ID:      169061078
Email:   tang1078@mylaurier.ca
__updated__ = "2024-03-08"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_code_bst, DATA1

bst = BST()

# Fill the BST with Morse code data
fill_code_bst(bst, DATA1)

# Print the BST
for each in bst.inorder():
    print(each)