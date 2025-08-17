"""This module provides a function to simulate a network connection."""
import time


def connect() -> None:
    """
    Simulates connecting to the internet.

    Prints a "Connecting" message, waits for 3 seconds,
    and then prints a "Connected" message.
    """
    print('Connecting to internet')
    time.sleep(3)
    print('you are connected')


if __name__ == '__main__':
    connect()
