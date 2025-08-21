"""
Slice Objects in Python

This script demonstrates the use of slice objects in Python for advanced sequence slicing.

Slice objects provide a way to store and reuse slicing parameters. They are particularly
useful when you need to apply the same slice operation multiple times or want to make
your code more readable by naming your slice operations.

Key benefits of slice objects:
- Reusability: Define once, use multiple times
- Readability: Give meaningful names to slice operations
- Flexibility: Can be stored in variables, passed to functions, etc.

Slice syntax: slice(start, stop, step)
- start: Starting index (None means start from beginning)
- stop: Ending index (None means go to end)
- step: Step size (negative values for reverse)
"""

# Create sample data
numbers: list[int] = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text: str = 'Hello, World!'

print(f"Original numbers: {numbers}")
print(f"Original text: '{text}'")
print()

# Create a slice object to reverse a sequence
# slice(None, None, -1) means start from end, go to beginning, step backwards by 1
rev: slice = slice(None, None, -1)

# Create a slice object to get the first five elements
# slice(None, 5) means start from beginning, go to index 5, default step of 1
first_five: slice = slice(None, 5)

# Create a slice object to get every other element
every_other: slice = slice(None, None, 2)

# Create a slice object to get the last three elements
last_three: slice = slice(-3, None)

print("Using slice objects:")
print(f"Reversed text: '{text[rev]}'")
print(f"First five numbers: {numbers[first_five]}")
print(f"Every other number: {numbers[every_other]}")
print(f"Last three numbers: {numbers[last_three]}")

print("\nEquivalent operations without slice objects:")
print(f"text[::-1] = '{text[::-1]}'")
print(f"numbers[:5] = {numbers[:5]}")
print(f"numbers[::2] = {numbers[::2]}")
print(f"numbers[-3:] = {numbers[-3:]}")

# Slice objects can also be used with other sequence types
data_tuple = (10, 20, 30, 40, 50)
print(f"\nTuple slicing: {data_tuple[first_five]}")
