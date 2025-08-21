"""
This module demonstrates the use of the walrus operator (:=),
introduced in Python 3.8.

The walrus operator is an assignment expression that allows you to
assign a value to a variable as part of a larger expression.
"""

users: dict[int, str] = {
    0: 'Bob',
    1: 'Mario'
}
# user: str | None = users.get(1)

# The walrus operator assigns the result of users.get(1) to 'user'
# and then checks if 'user' is truthy in the same line.
if user := users.get(1):
    print(f'{user} exists')
else:
    print('No user found')


def get_info(text: str) -> dict:
    """
    Analyzes a text string and returns a dictionary with details.

    This function uses the walrus operator to avoid calling text.split() twice.
    The result of text.split() is assigned to 'words' and reused to calculate
    word_count and character_count.

    Args:
        text: The input string to analyze.

    Returns:
        A dictionary containing the list of words, the word count,
        and the total character count (excluding spaces).
    """
    return {
        'words': (words := text.split()),
        'word_count': len(words),
        'character_count': len(''.join(words))
    }


print(get_info('Bob'))
print(get_info('Hello Bob'))
print(get_info('My name is Bob'))
