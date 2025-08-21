"""
Basic Python Data Types and Concepts

This module demonstrates fundamental Python data types and object-oriented programming concepts:
- Basic data types (int, float, str, bool)
- Collection types (list, tuple, set, dict)
- Type annotations
- Final constants
- DateTime operations
- Functions with type hints
- Class definition with special methods (__str__, __add__)

Each section shows practical usage with clear examples and documentation.
"""

from typing import Final
from datetime import datetime


def demonstrate_data_types() -> None:
    """Demonstrates basic Python data types."""
    print("=== Basic Data Types ===")

    # Numeric types
    number: int = 10
    decimal: float = 10.24

    # Text type
    text: str = 'hello world'

    # Boolean type
    active: bool = True

    print(f"Integer: {number}")
    print(f"Float: {decimal}")
    print(f"String: '{text}'")
    print(f"Boolean: {active}")
    print()


def demonstrate_collections() -> None:
    """Demonstrates Python collection types."""
    print("=== Collection Types ===")

    # List - mutable, ordered collection
    names: list = ['ted', 'sunil', 'omkar', 'rakshit']
    print(f"List: {names}")

    # Tuple - immutable, ordered collection
    coordinates: tuple = (1.5, 8.9)
    print(f"Tuple: {coordinates}")

    # Set - mutable, unordered collection of unique elements
    unique: set = {1, 4, 6, 8, 4}  # Duplicates are automatically removed
    print(f"Set: {unique}")

    # Dictionary - mutable, unordered key-value pairs
    data: dict = {
        'name': 'ted',
        'age': 24
    }
    print(f"Dictionary: {data}")
    print()


def demonstrate_type_annotations() -> None:
    """Demonstrates type annotations for better code documentation and IDE support."""
    print("=== Type Annotations ===")

    # Basic type annotations
    name: str = 'Ted'
    age: int = 19

    print(f"Name (str): {name}")
    print(f"Age (int): {age}")

    # Final constants - values that shouldn't be changed
    Pi: Final[float] = 3.142
    print(f"Pi constant: {Pi}")

    # Type annotations help with:
    # - Code documentation
    # - IDE support and autocompletion
    # - Static type checking with tools like mypy
    # - Better code readability

    print()


def demonstrate_datetime() -> None:
    """Demonstrates date and time operations."""
    print("=== DateTime Operations ===")

    current_time = datetime.now()
    print(f"Current date and time: {current_time}")
    print(f"Current date: {current_time.date()}")
    print(f"Current time: {current_time.time()}")
    print(f"Day: {current_time.day}")
    print(f"Month: {current_time.month}")
    print(f"Year: {current_time.year}")
    print()


def demonstrate_functions() -> None:
    """Demonstrates function definitions with type hints."""
    print("=== Functions with Type Hints ===")

    def greet(name: str) -> None:
        """Greets a person by name.

        Args:
            name: The name of the person to greet
        """
        print(f'Hello, {name}!')

    def add(a: float, b: float) -> float:
        """Adds two floating-point numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of the two numbers
        """
        return a + b

    # Function calls
    greet('Ted')
    greet('Sunil')

    result = add(10.9, 50.0)
    print(f"Addition result: {result}")
    print()


class Car:
    """
    A simple Car class demonstrating object-oriented programming concepts.

    This class shows:
    - Constructor (__init__)
    - Instance attributes
    - String representation (__str__)
    - Custom addition operation (__add__)
    """

    def __init__(self, brand: str, horsepower: int) -> None:
        """Initialize a Car object.

        Args:
            brand: The car's brand name
            horsepower: The car's horsepower rating
        """
        self.brand = brand
        self.horsepower = horsepower

    def drive(self) -> None:
        """Simulate the car driving."""
        print(f'{self.brand} is driving')

    def get_info(self) -> None:
        """Display information about the car."""
        print(f'{self.brand} with {self.horsepower} horsepower')

    def __str__(self) -> str:
        """Return a string representation of the car.

        Returns:
            String in format "brand, horsepower hp"
        """
        return f'{self.brand}, {self.horsepower}hp'

    def __add__(self, other: 'Car') -> str:
        """Combine two cars into a string representation.

        Args:
            other: Another Car object

        Returns:
            String combining both car brands
        """
        return f'{self.brand} and {other.brand}'


def demonstrate_classes() -> None:
    """Demonstrates class usage and special methods."""
    print("=== Class Demonstration ===")

    # Create car objects
    volvo: Car = Car('Volvo', 200)
    bmw: Car = Car('BMW', 240)

    # Use string representation
    print(f"Volvo car: {volvo}")
    print(f"BMW car: {bmw}")

    # Use custom addition
    print(f"Combined cars: {volvo + bmw}")

    # Demonstrate other methods
    volvo.drive()
    volvo.get_info()
    print()


def main() -> None:
    """Main function to run all demonstrations."""
    print("Basic Python Data Types and Concepts")
    print("=" * 45)

    demonstrate_data_types()
    demonstrate_collections()
    demonstrate_type_annotations()
    demonstrate_datetime()
    demonstrate_functions()
    demonstrate_classes()


if __name__ == '__main__':
    main()
