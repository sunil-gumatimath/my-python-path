def greet() -> None:
    """Greets the user."""
    print('Hello, World')


def bye() -> None:
    """Says goodbye to the user."""
    print('Bye, World')


def main() -> None:
    """Main function of the script."""
    greet()
    bye()


if __name__ == '__main__':
    # This ensures the main function is called only when the script is executed directly
    main()
