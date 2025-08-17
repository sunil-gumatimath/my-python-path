# Demonstrates self-documenting f-strings in Python.
# This feature is available in Python 3.8 and later.

a: int = 5
b: int = 10
my_var: str = 'bob says hi'

# The f-string syntax `{a + b = }` will print the expression `a + b`
# followed by its value.
print(f'{a + b=}')

# This also works with function calls inside the f-string.
print(f'{bool(a)=}')
