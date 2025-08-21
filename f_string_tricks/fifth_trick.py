"""
Self-Documenting F-Strings (Python 3.8+)

This script demonstrates self-documenting f-strings, a feature introduced in Python 3.8.
Self-documenting f-strings allow you to include both the expression and its value in the output,
making debugging and logging much more informative.

Syntax: f'{expression=}'
- Shows the expression text followed by its evaluated value
- Perfect for debugging and logging
- Works with variables, calculations, and function calls
"""

# Sample variables for demonstration
a: int = 5
b: int = 10
my_var: str = 'bob says hi'

print("Self-Documenting F-Strings Examples")
print("=" * 40)

# The f-string syntax `{a + b = }` will print the expression `a + b` followed by its value.
# Output: a + b = 15
print(f'{a + b=}')

# This also works with function calls inside the f-string.
# Output: bool(a) = True
print(f'{bool(a)=}')

# More examples
print(f'\nAdditional examples:')
print(f'{a=}')
print(f'{b=}')
print(f'{my_var=}')
print(f'{len(my_var)=}')
print(f'{my_var.upper()=}')
print(f'{a * b + 5=}')

print(f'\nComparison with regular f-strings:')
print(f'Regular: a + b = {a + b}')
print(f'Self-doc: {a + b=}')

print(f'\nPractical applications:')
print('- Debug logging')
print('- Scientific computing')
print('- Educational code')
print('- Interactive development')
print('- Quick value inspection')
