"""
Advanced Object-Oriented Programming - Special Methods (Dunder Methods)

This module demonstrates advanced OOP concepts using a Microwave class that showcases:
- Special methods (dunder methods) for operator overloading
- String representation methods (__str__ and __repr__)
- Custom object behavior through operator overloading
- Class state management

Special methods demonstrated:
- __init__: Constructor for object initialization
- __str__: Human-readable string representation
- __repr__: Developer-friendly string representation
- __add__: Overloading the + operator
- __mul__: Overloading the * operator
"""


class Microwave:
    """
    A Microwave class demonstrating advanced OOP concepts and operator overloading.

    This class represents a microwave oven with basic functionality and
    showcases Python's special methods (dunder methods) for customizing
    object behavior.

    Attributes:
        brand (str): The brand name of the microwave
        power_rating (str): The energy efficiency rating
        turned_on (bool): Current power state of the microwave

    Special Methods:
        __add__: Combines two microwaves with + operator
        __mul__: Combines two microwaves with * operator
        __str__: User-friendly string representation
        __repr__: Developer-friendly string representation
    """

    def __init__(self, brand: str, power_rating: str) -> None:
        """
        Initialize a new Microwave object.

        Args:
            brand: The brand name of the microwave
            power_rating: The energy efficiency rating (e.g., 'A', 'B', 'C')
        """
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        """Turn on the microwave."""
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned on')

    def turn_off(self) -> None:
        """Turn off the microwave."""
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave ({self.brand}) is now turned off')
        else:
            print(f'Microwave ({self.brand}) is already turned off')

    def run(self, seconds: int) -> None:
        """
        Run the microwave for a specified number of seconds.

        Args:
            seconds: Number of seconds to run the microwave
        """
        if self.turned_on:
            print(f'Running {self.brand} for {seconds} seconds')
        else:
            print(f'A mystical force whispers: Turn on your microwave')

    def __add__(self, other: 'Microwave') -> str:
        """
        Overload the + operator to combine two microwaves.

        Args:
            other: Another Microwave object

        Returns:
            String representation of the combination
        """
        return f'{self.brand} + {other.brand}'

    def __mul__(self, other: 'Microwave') -> str:
        """
        Overload the * operator to combine two microwaves.

        Args:
            other: Another Microwave object

        Returns:
            String representation of the combination
        """
        return f'{self.brand} * {other.brand}'

    def __str__(self) -> str:
        """
        Return a human-readable string representation.

        Returns:
            User-friendly string showing brand and rating
        """
        return f'{self.brand}(Rating: {self.power_rating})'

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation.

        Returns:
            String that could recreate the object
        """
        return f'Microwave(brand="{self.brand}", power_rating="{self.power_rating}")'


def main() -> None:
    """Demonstrate the Microwave class and its special methods."""
    print("Advanced OOP - Special Methods Demo")
    print("=" * 40)

    # Create microwave objects
    smeg: Microwave = Microwave('Smeg', 'B')
    bosch: Microwave = Microwave('Bosch', 'C')

    print("Operator Overloading:")
    print("-" * 20)
    print(f"Addition: {smeg + bosch}")
    print(f"Multiplication: {smeg * bosch}")
    print()

    print("String Representations:")
    print("-" * 25)
    print(f"__str__: {smeg}")
    print(f"__repr__: {repr(smeg)}")
    print(f"__str__: {bosch}")
    print()

    print("Microwave Operations:")
    print("-" * 22)
    smeg.turn_on()
    smeg.run(30)
    smeg.turn_off()
    print()

    print("Key OOP Concepts Demonstrated:")
    print("- Encapsulation (data + methods bundled together)")
    print("- Operator overloading (customizing +, *)")
    print("- String representation methods (__str__, __repr__)")
    print("- Type annotations for better code documentation")
    print("- State management (turned_on attribute)")


if __name__ == '__main__':
    main()
