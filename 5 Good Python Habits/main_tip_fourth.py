from typing import List

def upper_everything(elements: List[str]) -> List[str]:
    """Converts a list of strings to uppercase using type annotations.

    Type annotations are a feature of Python that allow you to add type hints to variables,
    function parameters, and function return values. These hints can help you write more
    readable and maintainable code, and they can also be used by tools like type checkers
    to find errors in your code.

    In this function, the type annotation `elements: List[str]` indicates that the `elements`
    parameter is expected to be a list of strings. The type annotation `-> List[str]`
    indicates that the function is expected to return a list of strings.

    Args:
        elements (List[str]): A list of strings to be converted to uppercase.

    Returns:
        List[str]: A new list containing the uppercase versions of the input strings.
    """
    return [element.upper() for element in elements]


# The following line creates a list of strings and converts them to uppercase using the
# `upper_everything` function. The type annotation `loud_list: List[str]` indicates that
# the `loud_list` variable is expected to be a list of strings.
loud_list: List[str] = upper_everything(['mario', 'james', 'sandra'])

# The following line will cause a type hint error because the `upper_everything` function
# is annotated to return a `List[str]`, but the `loud_list_2` variable is annotated
# as `List[int]`. This mismatch can be caught by a type checker.
loud_list_2: List[int] = upper_everything(['mario', 'james', 'sandra'])


# Print the loud_list to the console.
print(loud_list)