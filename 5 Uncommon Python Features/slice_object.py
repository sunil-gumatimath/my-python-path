"""
This script demonstrates the use of the slice object in Python.

A slice object can be used to specify how to slice a sequence.
You can use them to make your code more readable and reusable.
"""

# Create a list of numbers from 1 to 10
numbers: list[int] = list(range(1, 11))
# Create a sample string
text: str = 'Hello, World!'

# Create a slice object to reverse a sequence
# slice(start, stop, step)
rev: slice = slice(None, None, -1)

# Create a slice object to get the first five elements
f_five: slice = slice(None, 5)

# The following lines are equivalent to using the slice objects directly
# print(numbers[::-1])
# print(text[::-1])

# Use the slice object to reverse the string
print(text[rev])

# Use the slice object to get the first five numbers
print(numbers[f_five])
