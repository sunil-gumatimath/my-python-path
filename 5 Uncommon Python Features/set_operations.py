"""
Set Operations in Python

This script demonstrates the fundamental set operations in Python:
- Union: Combines elements from both sets (no duplicates)
- Intersection: Finds common elements between sets
- Difference: Finds elements in one set but not the other
- Symmetric Difference: Finds elements in either set but not both

Sets in Python are unordered collections of unique elements that support
mathematical set operations. They are useful for:
- Removing duplicates from collections
- Checking membership efficiently
- Performing mathematical set operations
- Finding unique elements across multiple collections
"""

# Define two sample sets for demonstration
set_a: set[int] = {1, 2, 3, 4, 5}
set_b: set[int] = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print()

# Union of two sets - combines all unique elements from both sets
# Result: {1, 2, 3, 4, 5, 6, 7, 8}
print("Union (set_a | set_b) - all elements from both sets:")
print(set_a | set_b)

# Intersection of two sets - elements common to both sets
# Result: {4, 5}
print("\nIntersection (set_a & set_b) - common elements:")
print(set_a & set_b)

# Difference of two sets - elements in set_a but not in set_b
# Result: {1, 2, 3}
print("\nDifference (set_a - set_b) - elements only in set_a:")
print(set_a - set_b)

# Difference of two sets - elements in set_b but not in set_a
# Result: {6, 7, 8}
print("\nDifference (set_b - set_a) - elements only in set_b:")
print(set_b - set_a)

# Symmetric difference of two sets - elements in either set but not both
# Result: {1, 2, 3, 6, 7, 8}
print("\nSymmetric difference (set_a ^ set_b) - elements in either set but not both:")
print(set_a ^ set_b)

print("\nAdditional set methods available:")
print(f"set_a.isdisjoint(set_b): {set_a.isdisjoint(set_b)}")  # True if no common elements
print(f"set_a.issubset(set_b): {set_a.issubset(set_b)}")      # True if set_a is subset of set_b
print(f"set_a.issuperset(set_b): {set_a.issuperset(set_b)}") # True if set_a contains set_b
