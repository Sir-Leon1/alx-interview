#!/usr/bin/python3
"""
Main file for testing
"""

island_perimeter = __import__('0-island_perimeter').island_perimeter

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Expected output: 12
