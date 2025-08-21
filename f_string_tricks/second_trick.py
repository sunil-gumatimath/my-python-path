"""
F-String Text Alignment and Padding

This script demonstrates how to use f-strings for text alignment and padding.
F-strings allow you to control the alignment and padding of text within a specified width.

Format specifiers for alignment:
- > : Right-align
- < : Left-align
- ^ : Center-align

Format syntax: f'{value:padding_character alignment width}'
"""

# Assign the string to demonstrate alignment techniques
var: str = 'ted'

print("F-String Text Alignment Examples")
print("=" * 35)
print(f"Original text: '{var}'")
print(f"Length: {len(var)} characters")
print()

# Right-align the string within a 20-character width, padding with underscores
# Format: _>20 means "pad with underscores, right-align, total width 20"
print(f"Right-aligned (underscores): '{var:_>20}'")

# Left-align the string within a 20-character width, padding with hash symbols
# Format: #<20 means "pad with hashes, left-align, total width 20"
print(f"Left-aligned (hashes): '{var:#<20}'")

# Center the string within a 20-character width, padding with pipe symbols
# Format: |^20 means "pad with pipes, center-align, total width 20"
print(f"Center-aligned (pipes): '{var:|^20}'")

print()
print("Alignment format syntax: f'{value:padding_char alignment width}'")
print("Where:")
print("- padding_char: Character to use for padding (optional)")
print("- alignment: < (left), > (right), ^ (center)")
print("- width: Total width of the formatted string")

# More examples with different characters
text = "Python"
print(f"\nAdditional examples with '{text}':")
print(f"Right with spaces: '{text:>10}'")
print(f"Left with dots: '{text:.<10}'")
print(f"Center with stars: '{text:*^10}'")
print(f"No padding needed: '{text:>6}'")

print(f"\nPractical uses:")
print("- Creating tables with aligned columns")
print("- Formatting headers and titles")
print("- Creating ASCII art")
print("- Professional text output formatting")
