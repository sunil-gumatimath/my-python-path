"""
Inheritance - Object-Oriented Programming Example

This module demonstrates inheritance, one of the fundamental concepts of object-oriented programming.
Inheritance allows one class (child/subclass) to inherit attributes and methods from another class (parent/superclass).

Key concepts demonstrated:
- Base class (Animal) with common attributes and methods
- Derived classes (Dog, Cat, Mouse) that inherit from the base class
- Method overriding (each animal has its own speak method)
- Polymorphism (different objects respond differently to the same method call)

The example shows how inheritance promotes code reuse and creates a natural hierarchy.
"""


class Animal:
    """
    Base class representing a generic animal.

    This parent class defines common characteristics and behaviors
    that all animals share, such as having a name, being alive,
    and performing basic life functions like eating and sleeping.

    Attributes:
        name (str): The name of the animal
        is_alive (bool): Whether the animal is alive (always True for new animals)
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a new Animal.

        Args:
            name: The name of the animal
        """
        self.name = name
        self.is_alive = True

    def eat(self) -> None:
        """Simulate the animal eating."""
        print(f'{self.name} is eating')

    def sleep(self) -> None:
        """Simulate the animal sleeping."""
        print(f'{self.name} is sleeping')


class Dog(Animal):
    """
    Dog class that inherits from Animal.

    Dogs inherit all attributes and methods from Animal,
    and add their own specific behavior (speaking).
    """

    def speak(self) -> None:
        """Make the dog speak (woof)."""
        print('Woof!')


class Cat(Animal):
    """
    Cat class that inherits from Animal.

    Cats inherit all attributes and methods from Animal,
    and add their own specific behavior (speaking).
    """

    def speak(self) -> None:
        """Make the cat speak (meow)."""
        print('Meow!')


class Mouse(Animal):
    """
    Mouse class that inherits from Animal.

    Mice inherit all attributes and methods from Animal,
    and add their own specific behavior (speaking).
    """

    def speak(self) -> None:
        """Make the mouse speak (squeak)."""
        print('Squeek!')


def demonstrate_inheritance() -> None:
    """Demonstrate inheritance and polymorphism with different animals."""
    # Create instances of different animals
    dog = Dog('Bruno')
    cat = Cat('Tom')
    mouse = Mouse('Jerry')

    print("Inheritance and Polymorphism Demo")
    print("=" * 35)

    # Each animal has access to inherited attributes and methods
    print("Dog:")
    print(f"Name: {dog.name}")
    print(f"Alive: {dog.is_alive}")
    dog.speak()  # Dog's specific method
    dog.eat()    # Inherited method
    print()

    print("Cat:")
    print(f"Name: {cat.name}")
    print(f"Alive: {cat.is_alive}")
    cat.speak()  # Cat's specific method
    cat.sleep()  # Inherited method
    print()

    print("Mouse:")
    print(f"Name: {mouse.name}")
    print(f"Alive: {mouse.is_alive}")
    mouse.speak()  # Mouse's specific method
    print()


if __name__ == '__main__':
    demonstrate_inheritance()
