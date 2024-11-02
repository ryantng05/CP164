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
from morse import fill_letter_bst, DATA1

bst = BST()

fill_letter_bst(bst, DATA1)

for each in bst.inorder():
    print(each)