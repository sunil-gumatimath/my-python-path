"""
Union Types in Type Annotations

This example demonstrates the use of union types in Python type annotations.
Union types allow you to specify that a variable can be one of several types.

The `str | int` syntax (available in Python 3.10+) indicates that each element
in the list can be either a string or an integer. This is equivalent to
`Union[str, int]` from the typing module.

Type annotations with union types help with:
- Code readability and documentation
- IDE support and autocompletion
- Static type checking with tools like mypy

Example usage:
- Lists with mixed data types
- Function parameters that accept multiple types
- Variables that can change type based on conditions
"""

# This list demonstrates a mix of string and integer types using union type annotations.
# The `str | int` annotation indicates each element can be either a string or integer.
sample: list[str | int] = ['a', 1, 'b', 2]

# You can also use the Union type from typing module (compatible with older Python versions):
# from typing import Union
# sample: list[Union[str, int]] = ['a', 1, 'b', 2]
