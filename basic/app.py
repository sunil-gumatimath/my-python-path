"""
Basic Python Concepts Demonstration

This module demonstrates fundamental Python concepts including:
- String manipulation methods
- Arithmetic operations
- Conditional statements (if/elif/else, ternary operator)
- Loops (for, while)
- Function definitions with default arguments and *args
- Input/Output operations

Each section is organized and documented to show practical usage of basic Python features.
"""

import math


def demonstrate_string_methods() -> None:
    """Demonstrates various string manipulation methods in Python."""
    print("=== String Methods Demo ===")
    full_name = ' sunil gumatimath '

    print(f"Original: '{full_name}'")
    print(f"Uppercase: '{full_name.upper()}'")
    print(f"Lowercase: '{full_name.lower()}'")
    print(f"Title case: '{full_name.title()}'")
    print(f"Right strip: '{full_name.rstrip()}'")
    print(f"Find 'math': {full_name.find('math')}")
    print(f"Replace 'math' with 'MATH': '{full_name.replace('math', 'MATH')}'")
    print(f"'il' in name: {'il' in full_name}")
    print(f"'vai' not in name: {'vai' not in full_name}")
    print()


def demonstrate_arithmetic() -> None:
    """Demonstrates basic arithmetic operations and math functions."""
    print("=== Arithmetic Operations Demo ===")

    # Basic arithmetic
    print("Basic operations:")
    print(f"10 + 3 = {10 + 3}")
    print(f"10 - 3 = {10 - 3}")
    print(f"10 * 3 = {10 * 3}")
    print(f"10 / 3 = {10 / 3}")
    print(f"10 // 3 = {10 // 3}")  # Floor division
    print(f"10 % 3 = {10 % 3}")   # Modulo
    print(f"10 ** 3 = {10 ** 3}") # Exponentiation

    # Math functions
    print("\nMath functions:")
    print(f"round(2.9) = {round(2.9)}")
    print(f"round(2.4) = {round(2.4)}")
    print(f"abs(-2.6) = {abs(-2.6)}")
    print(f"math.ceil(2.2) = {math.ceil(2.2)}")
    print()


def demonstrate_conditionals() -> None:
    """Demonstrates conditional statements and logical operators."""
    print("=== Conditional Statements Demo ===")

    # Basic if-elif-else
    temp = 35
    if temp >= 35:
        print('Temperature is warm')
        print('Remember to drink water')
    elif temp > 20:
        print('Temperature is comfortable')
    print('Done checking temperature')
    print()

    # If-else with variable assignment
    age = 24
    if age > 18:
        message = 'You are eligible'
    else:
        message = 'You are a minor'
    print(f"Age check: {message}")

    # Ternary operator
    message = "Eligible" if age >= 18 else "Not Eligible"
    print(f"Ternary result: {message}")
    print()

    # Logical operators
    high_income = True
    good_credit = True
    student = True

    if high_income or good_credit:
        print('Eligible for loan')
    else:
        print('Not eligible for loan')

    if (high_income or good_credit) and not student:
        print('Eligible for premium loan')
    else:
        print('Not eligible for premium loan')

    # Chained comparison
    if 18 <= age < 80:
        print('Age is within valid range')
    print()


def demonstrate_loops() -> None:
    """Demonstrates various loop constructs in Python."""
    print("=== Loops Demo ===")

    # For loop with range
    print("For loop with step:")
    for num in range(1, 10, 2):
        print(f'Attempt {num} {"." * (num + 1)}')
    print()

    # For loop with break/else
    successful = False
    for num in range(3):
        print('Attempting operation...')
        if successful:
            print('Operation successful!')
            break
    else:
        print('Attempted 3 times and failed')
    print()

    # Nested loops
    print("Nested loops (5x3 grid):")
    for x in range(5):
        for y in range(3):
            print(f'{x}, {y}')
    print()

    # Loop through list
    print("Loop through list:")
    for x in [1, 2, 3, 4]:
        print(f'Item: {x}')
    print()

    # While loop
    print("While loop (halving numbers):")
    number = 100
    while number > 0:
        print(f'Current: {number}')
        number //= 2
    print()


def demonstrate_functions() -> None:
    """Demonstrates function definitions and usage."""
    print("=== Functions Demo ===")

    def greet(name: str) -> None:
        """Greets a person by name."""
        print(f'Hello {name}!')

    def get_greeting(name: str) -> str:
        """Returns a greeting message for the given name."""
        return f'Hi {name}!'

    def increment(num: int, by: int = 1) -> int:
        """Increments a number by a specified amount (default 1)."""
        return num + by

    def multiply(*numbers: int) -> int:
        """Multiplies all provided numbers together."""
        total = 1
        for num in numbers:
            total *= num
        return total

    # Function calls
    greet('Ted')

    message = get_greeting('Ted')
    print(message)

    print(f"increment(2, 5) = {increment(2, 5)}")
    print(f"increment(5) = {increment(5)}")  # Uses default 'by=1'

    print(f"multiply(2, 3, 4, 5) = {multiply(2, 3, 4, 5)}")
    print()


def count_even_numbers() -> None:
    """Counts and displays even numbers in a range."""
    print("=== Even Numbers Counter ===")
    count = 0

    for num in range(1, 10):
        if num % 2 == 0:
            count += 1
            print(f'Even number: {num}')

    print(f'We have {count} even numbers')
    print()


def main() -> None:
    """Main function to run all demonstrations."""
    print("Python Basic Concepts Demonstration")
    print("=" * 40)

    demonstrate_string_methods()
    demonstrate_arithmetic()
    demonstrate_conditionals()
    demonstrate_loops()
    count_even_numbers()
    demonstrate_functions()


if __name__ == '__main__':
    main()
