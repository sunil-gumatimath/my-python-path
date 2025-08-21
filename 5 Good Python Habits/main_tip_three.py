def is_an_adult(age, has_id) -> bool:
    """
    Checks if a person is of legal age and has an ID.

    Args:
        age: The person's age.
        has_id: Whether the person has an ID.

    Returns:
        True if the person is 21 or older and has an ID, False otherwise.
    """
    return age >= 21 and has_id


def is_bob(name) -> bool:
    """
    Checks if a person's name is Bob.

    Args:
        name: The person's name.

    Returns:
        True if the name is 'bob' (case-insensitive), False otherwise.
    """
    return name.lower() == 'bob'


def entry_club(name, age, has_id) -> None:
    """
    Determines if a person is allowed to enter the club.

    Args:
        name: The person's name.
        age: The person's age.
        has_id: Whether the person has an ID.
    """
    if is_bob(name):
        print('get out of here Bob, we don\'t want no trouble ')
        return

    if is_an_adult(age, has_id):
        print('you may enter the club')
    else:
        print('you may not enter the club')


def main() -> None:
    """Main function to demonstrate the entry_club functionality."""
    entry_club('Bob', 29, has_id=True)
    entry_club('james', 28, has_id=True)
    entry_club('jimmy', 22, has_id=False)
    entry_club('Tom', 20, has_id=True)


if __name__ == '__main__':
    main()
