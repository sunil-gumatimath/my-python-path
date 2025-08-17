# Assign a large integer to the variable 'n'
n: int = 100000000

# Use an f-string to print the number with underscores as thousand separators.
# This can improve readability for large numbers.
print(f'{n:_}')

# Use an f-string to print the number with commas as thousand separators.
# This is a common way to format numbers in many regions.
print(f'{n:,}')
