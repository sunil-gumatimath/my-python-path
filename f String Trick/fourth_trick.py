# Define a floating-point number
n: float = 1234.5678

# Format the number to two decimal places
print(f'Result: {n:.2f}')

# Format the number to zero decimal places
print(f'Result: {n:.0f}')

# Format the number with a comma as a thousands separator and three decimal places
print(f'Result: {n:,.3f}')

# Round the number to two decimal places using the round() function
print(round(n, 2))
