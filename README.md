# Python Practice Repository

This repository contains various Python practice scripts covering fundamental concepts and object-oriented programming.

## Directory Structure

- `basic/`: Contains basic Python scripts demonstrating fundamental concepts like data types, operators, conditional statements, loops, functions, and basic input/output.
  - `app.py`: Includes examples of string manipulation, arithmetic operations, conditional logic (if/elif/else, ternary operator), loops (for, while), and function definitions (with default arguments and `*args`).
  - `main.py`: Demonstrates basic data types (int, float, str, bool, list, tuple, set, dict), type annotations, `Final` keyword, `datetime` module usage, and a simple `Car` class with `__str__` and `__add__` methods.

- `f_string_tricks/`: Focuses on various f-string formatting techniques.
  - `first_trick.py`: Shows how to format large integers with underscores and commas for readability.
  - `second_trick.py`: Demonstrates string alignment (right, left, center) with custom padding characters.
  - `third_trick.py`: Illustrates formatting `datetime` objects using various format codes.
  - `fourth_trick.py`: Provides examples of formatting floating-point numbers to specific decimal places and with thousands separators.
  - `fifth_trick.py`: Demonstrates self-documenting f-strings (Python 3.8+), which print the expression and its value.

- `object_oriented/`: Contains examples of Object-Oriented Programming (OOP) concepts.
  - `car.py`: Defines a `Car` class with attributes (make, model, year, color) and methods (`drive`, `stop`).
  - `inheritance.py`: Demonstrates inheritance with an `Animal` base class and `Dog`, `Cat`, `Mouse` subclasses, each with a `speak` method.
  - `main.py`: Imports and uses the `Car` class from `car.py`, creating `Car` objects and calling their methods.

- `oops_concepts/`: Another directory for Object-Oriented Programming examples.
  - `oop.py`: Defines a `Microwave` class with methods for turning on/off, running, and custom `__add__`, `__mul__`, `__str__`, and `__repr__` methods.

- `5 Good Python Habits/`: Contains scripts demonstrating good Python programming practices.
  - `main_tip_fifth.py`: Demonstrates list comprehensions for concise list creation.
  - `main_tip_fourth_1.py`: Illustrates type annotations for function parameters and return values, and how type checkers can use them.
  - `main_tip_fourth_2.py`: Shows type annotation for a list with mixed types (`str | int`).
  - `main_tip_three.py`: Demonstrates clear function definitions and early exit conditions for improved readability and maintainability.
  - `main_tip_two.py`: Illustrates the use of `if __name__ == '__main__':` to ensure functions are called only when the script is executed directly.
  - `model_main_tips_one.py`: Shows how to import and use functions from other modules, promoting modularity.
  - `module.py`: Defines a simple `connect` function to simulate a network connection, used by `model_main_tips_one.py`.

- `5 Uncommon Python Features/`: Contains scripts demonstrating lesser-known but powerful Python features.
  - `currying.py`: Demonstrates function currying, a technique where a function that takes multiple arguments is transformed into a sequence of functions each taking a single argument.
  - `formate.py`: Shows how to use the `__format__` dunder method to create custom string formatting for objects using f-strings with format specifiers.
  - `set_operations.py`: Demonstrates Python's set operations including union, intersection, difference, and symmetric difference with practical examples and additional set methods.
  - `slice_object.py`: Shows how to use slice objects for reusable slicing operations, including advanced examples with different sequences and step values.
  - `walrus_operator.py`: Demonstrates the walrus operator (:=) for assignment expressions, showing its use in conditional statements and function calls.

## Documentation

All Python files in this repository now include comprehensive documentation with:
- Detailed module-level docstrings explaining the purpose and concepts demonstrated
- Function and method docstrings with parameter descriptions and return value information
- Inline comments explaining complex logic and Python features
- Usage examples and practical applications
- Type annotations for better code documentation and IDE support

Each file has been enhanced to serve as both a working example and a learning resource.

## How to Run

To run any of the Python scripts, navigate to the respective directory in your terminal and execute the script using Python:

```bash
python your_script_name.py
```

For example:

```bash
python basic/app.py
```

Many scripts now include a `main()` function and use the `if __name__ == '__main__':` pattern for better organization and reusability.

## Learning Outcomes

This repository covers a comprehensive range of Python programming concepts:

- **Basic Python**: Data types, operators, control flow, functions, and modules
- **Advanced String Formatting**: F-strings with numbers, alignment, datetime, and self-documenting expressions
- **Object-Oriented Programming**: Classes, inheritance, polymorphism, and special methods
- **Python Best Practices**: Type annotations, list comprehensions, modular code organization
- **Uncommon Features**: Currying, set operations, slice objects, walrus operator, and custom formatting

Each concept is presented with practical examples, detailed documentation, and clear explanations suitable for both beginners and intermediate Python developers.

## Recent Fixes

- **5 Good Python Habits/main_tip_three.py**: Corrected a syntax error in the `entry_club` function where `is_bob(name):` was missing an `if` statement, leading to a `Pylance Error: Expected expression`. The line was updated to `if is_bob(name):`.
- **Comprehensive Documentation**: Added detailed docstrings, type annotations, and examples to all Python files throughout the repository for better learning and maintainability.
