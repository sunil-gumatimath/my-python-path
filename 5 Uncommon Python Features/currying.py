"""
This script demonstrates the concept of currying in Python.

Currying is a technique in functional programming where a function that takes multiple arguments is transformed into a sequence of functions, each taking a single argument.

In this example, `multiply_setup` is a higher-order function that takes an argument `a` and returns a new function `multiply`. The returned function `multiply` "remembers" the value of `a` and takes a single argument `b` to complete the multiplication.

We create specialized functions `double` and `triple` by calling `multiply_setup` with 2 and 3 respectively. These new functions can then be used to multiply any number by 2 or 3.
"""
from typing import Callable


def multiply_setup(a: float) -> Callable:
    def multiply(b: float) -> float:
        return a*b

    return multiply


double: Callable = multiply_setup(2)
triple: Callable = multiply_setup(3)

print(double(5))
print(double(3))
print(double(100))


print(triple(5))
print(triple(3))
print(triple(100))
