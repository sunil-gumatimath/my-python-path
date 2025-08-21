"""
This script demonstrates how to use the __format__ dunder method to create
custom string formatting for objects.
"""
from typing import Any


class Book:
    """A simple class representing a book."""

    def __init__(self, title: str, pages: int) -> None:
        """Initializes a Book object.

        Args:
            title: The title of the book.
            pages: The number of pages in the book.
        """
        self.title = title
        self.pages = pages

    def __format__(self, format_spec: Any) -> str:
        """Provides custom formatting for the Book object.

        This method is called when the object is used in an f-string with a
        format specifier.

        Args:
            format_spec: The format specifier provided in the f-string.

        Returns:
            The formatted string.

        Raises:
            ValueError: If the format specifier is unknown.
        """
        match format_spec:
            case 'time':
                # Calculates the time to read the book in hours.
                return f'{self.pages / 60:.2f}h'
            case 'caps':
                # Returns the title of the book in uppercase.
                return self.title.upper()
            case _:
                raise ValueError(f'Unknown specifier for Book()')


def main() -> None:
    """
    Demonstrates the custom formatting of Book objects.
    """
    python_daily: Book = Book('Python Daily', 20)
    java_daily: Book = Book('Java Programming', 200)

    # Using the 'caps' format specifier to print the title in uppercase.
    print(f'{python_daily:caps}')
    # Using the 'time' format specifier to print the estimated reading time.
    print(f'Read time: {python_daily:time}')


if __name__ == '__main__':
    main()
