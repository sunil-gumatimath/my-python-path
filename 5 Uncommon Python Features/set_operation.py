"""
This script demonstrates the use of set operations in Python.
"""

set_a: set[int] = {1, 2, 3, 4, 5}
set_b: set[int] = {4, 5, 6, 7, 8}


# Union of two sets
print(set_a | set_b)

# Intersection of two sets
print(set_a & set_b)

# Difference of two sets (elements in set_a but not in set_b)
print(set_a - set_b)

# Difference of two sets (elements in set_b but not in set_a)
print(set_b - set_a)

# Symmetric difference of two sets (elements in either set_a or set_b, but not both)
print(set_a ^ set_b)
