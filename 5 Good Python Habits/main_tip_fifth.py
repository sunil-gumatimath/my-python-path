"""
List Comprehensions: A concise way to create lists.

Syntax: `[expression for item in iterable if condition]`

- `expression`: What to include in the new list.
- `item`: Current element from the `iterable`.
- `iterable`: The sequence to loop through.
- `condition` (optional): Filters items.

Example: `long_names = [people for people in peoples if len(people) > 7]`
This creates a list `long_names` containing `people` from `peoples` where the `len(people)` is greater than 7.
"""


peoples: list[str] = ['James', 'Charlotte', 'Stephany', 'Mario', 'Sandra']


# long_names: list[str] = []

# for person in people:
#     if len(person) > 7:
#         long_names.append(person)


long_names: list[str] = [people for people in peoples if len(people) > 7]

print(f'Long names: {long_names}')

# print(f'Long names: {[p for p in people if len(people) > 7]}')
