"""
Object-Oriented Programming - Car Class Usage Example

This module demonstrates how to use the Car class defined in car.py.
It shows:
- Importing classes from other modules
- Creating object instances
- Accessing object attributes
- Calling object methods
- Working with multiple objects of the same class

This example creates two Car objects and demonstrates their properties and behaviors.
"""

from car import Car


def main() -> None:
    """Main function demonstrating Car class usage."""
    print("Object-Oriented Programming - Car Class Demo")
    print("=" * 45)

    # Create two Car objects with different properties
    car_1 = Car('Chevrolet', 'Corvette', 2021, 'Red')
    car_2 = Car('Ford', 'Mustang', 2022, 'Black')

    print("First Car Details:")
    print("-" * 20)
    # Access the car's attributes
    print(f"Make: {car_1.make}")
    print(f"Model: {car_1.model}")
    print(f"Year: {car_1.year}")
    print(f"Color: {car_1.color}")

    # Call the car's methods
    print("Actions:")
    car_1.drive()
    car_1.stop()
    print()

    print("Second Car Details:")
    print("-" * 20)
    # Access the second car's attributes
    print(f"Make: {car_2.make}")
    print(f"Model: {car_2.model}")
    print(f"Year: {car_2.year}")
    print(f"Color: {car_2.color}")

    # Call the second car's methods
    print("Actions:")
    car_2.drive()
    car_2.stop()
    print()

    # Demonstrate the get_description method (if available)
    print("Complete Descriptions:")
    print(f"Car 1: {car_1.get_description()}")
    print(f"Car 2: {car_2.get_description()}")


if __name__ == '__main__':
    main()
