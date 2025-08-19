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

## How to Run

To run any of the Python scripts, navigate to the respective directory in your terminal and execute the script using Python:

```bash
python your_script_name.py
```

For example:

```bash
python basic/app.py
```

## Recent Fixes

- **5 Good Python Habits/main_tip_three.py**: Corrected a syntax error in the `entry_club` function where `is_bob(name):` was missing an `if` statement, leading to a `Pylance Error: Expected expression`. The line was updated to `if is_bob(name):`.
