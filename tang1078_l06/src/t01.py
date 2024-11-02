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

playlist = List()

playlist.prepend("Avicci - The Nights")

playlist.append("Believer - Imagine Dragons")

playlist.insert(1, "Im Good (Blue) -  Bebe Rexha and David Guetta")

for each in playlist:
    print(each)