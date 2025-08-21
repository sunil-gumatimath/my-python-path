"""
F-String Floating-Point Number Formatting

This script demonstrates how to use f-strings to format floating-point numbers.
F-strings provide precise control over decimal places, thousands separators, and number presentation.

Format syntax: f'{number:.precision f}'
- precision: Number of decimal places
- f: Fixed-point notation
- ,: Thousands separator (optional)

Key differences:
- f-string formatting: Changes display format only
- round() function: Actually changes the numeric value
"""

# Define a floating-point number for demonstration
n: float = 1234.5678

print("F-String Floating-Point Formatting Examples")
print("=" * 45)
print(f"Original number: {n}")
print()

# Format the number to two decimal places
print(f'Two decimal places: {n:.2f}')

# Format the number to zero decimal places
print(f'No decimal places: {n:.0f}')

# Format the number with a comma as a thousands separator and three decimal places
print(f'With thousands separator: {n:,.3f}')

# Round the number to two decimal places using the round() function
# Note: This actually changes the value, unlike f-string formatting
rounded = round(n, 2)
print(f'Rounded with round() function: {rounded}')

print()
print("Formatting options:")
print(":.2f - Two decimal places")
print(":.0f - No decimal places (integer-like)")
print(":,.3f - Three decimal places with thousands separator")
print(":.4f - Four decimal places")

# Additional examples
print(f"\nMore examples:")
print(f"Scientific notation: {n:.2e}")
print(f"Percentage: {0.856:.1%}")
print(f"Fixed width: {n:10.2f}")

print(f"\nPractical applications:")
print("- Currency formatting")
print("- Scientific data presentation")
print("- Financial reports")
print("- User interface displays")
