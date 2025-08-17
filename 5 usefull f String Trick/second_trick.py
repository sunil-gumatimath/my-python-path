# Assign the string 'ted' to the variable 'var'
var: str = 'ted'

# Right-align the string within a 20-character width, padding with underscores
print(f'{var:_>20}')

# Left-align the string within a 20-character width, padding with hash symbols
print(f'{var:#<20}')

# Center the string within a 20-character width, padding with pipe symbols
print(f'{var:|^20}')
