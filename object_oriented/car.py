"""
Car Class - Object-Oriented Programming Example

This module defines a Car class that demonstrates basic object-oriented programming concepts:
- Class definition
- Constructor (__init__ method)
- Instance attributes
- Instance methods
- Object creation and usage

The Car class represents a vehicle with properties like make, model, year, and color,
and provides methods to simulate driving and stopping behaviors.
"""


class Car:
    """
    A simple Car class representing a vehicle.

    This class demonstrates fundamental OOP concepts including encapsulation,
    where data (attributes) and behavior (methods) are bundled together.

    Attributes:
        make (str): The manufacturer of the car (e.g., 'Toyota', 'Ford')
        model (str): The model name of the car (e.g., 'Camry', 'Mustang')
        year (int): The manufacturing year of the car
        color (str): The color of the car

    Methods:
        drive(): Simulates the car driving
        stop(): Simulates the car stopping
    """

    def __init__(self, make: str, model: str, year: int, color: str) -> None:
        """
        Initialize a new Car object.

        Args:
            make: The manufacturer of the car
            model: The model name of the car
            year: The manufacturing year
            color: The color of the car
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self) -> None:
        """Simulate the car driving by printing a driving message."""
        print(f'This {self.model} is driving')

    def stop(self) -> None:
        """Simulate the car stopping by printing a stopping message."""
        print(f'This {self.model} has stopped')

    def get_description(self) -> str:
        """
        Get a complete description of the car.

        Returns:
            A string describing the car's make, model, year, and color
        """
        return f"{self.year} {self.color} {self.make} {self.model}"


# Example usage (only runs if this file is executed directly)
if __name__ == '__main__':
    # Create a car object
    my_car = Car('Toyota', 'Camry', 2022, 'Blue')

    # Use the car methods
    print("Car information:")
    print(f"Description: {my_car.get_description()}")
    my_car.drive()
    my_car.stop()
