"""
F-String Number Formatting - Thousands Separators

This script demonstrates how to use f-strings to format large numbers with thousands separators.
F-strings (formatted string literals) provide a concise way to embed expressions inside string literals.

Two common thousands separators are shown:
1. Underscore (_) - Useful for Python code and data processing
2. Comma (,) - Standard formatting for human-readable numbers

These formatting options make large numbers much more readable and professional-looking.
"""

# Assign a large integer to demonstrate number formatting
n: int = 100_000_000  # Using underscore for readability in code

print("F-String Number Formatting Examples")
print("=" * 40)
print(f"Original number: {n}")
print()

# Use underscore as thousands separator - great for code and technical contexts
# Output: 100_000_000
print(f"With underscores: {n:_}")

# Use comma as thousands separator - standard for human-readable numbers
# Output: 100,000,000
print(f"With commas: {n:,}")

print()
print("Benefits of thousands separators:")
print("- Improved readability for large numbers")
print("- Professional appearance in reports")
print("- Easier to parse mentally")
print("- Different separators for different contexts")

# Example with different number sizes
small_num: int = 1_234
medium_num: int = 12_345_678
large_num: int = 1_234_567_890

print(f"\nDifferent number sizes:")
print(f"Small: {small_num:,}")
print(f"Medium: {medium_num:,}")
print(f"Large: {large_num:,}")
