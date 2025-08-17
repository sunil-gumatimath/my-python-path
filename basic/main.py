# Basic Data Types
# number: int = 10
# decimal: float = 10.24
# text: str = 'hello world'
# active: bool = True


# names: list = ['ted', 'sunil', 'omkar', 'rakshit']
# coordinates: tuple = (1.5, 8.9)
# unique: set = {1, 4, 6, 8, 4}
# data: dict = {
#     'name': 'ted',
#     'age': 24
# }

# Type annotation
# name: str = 'Ted'
# age: int = 19

# from typing import Final
# Pi: Final[float] = 3.142

# from datetime import datetime


# def show_date() -> None:
#     print('This is the current date and time')
#     print(datetime.now())


# show_date()

# def greet(name) -> None:
#     print(f'hello, {name}')


# greet('ted')
# greet('sunil')

# def add(a: float, b: float) -> float:
#     return a+b


# print(add(10.9, 50.0))

class Car:
    def __init__(self, brand, horsepower) -> None:
        self.brand = brand
        self.horsepower = horsepower

    # def drive(self) -> None:
    #     print(f'{self.brand} is driving')

    # def get_info(self) -> None:
    #     print(f'{self.brand} with {self.horsepower} horsepower')

    def __str__(self) -> str:
        return f'{self.brand}, {self.horsepower}hp'

    def __add__(self, other) -> str:
        return 'f{self.brand}, {other.brand}'


volvo: Car = Car('volvo', 200)
print(volvo)

BMW: Car = Car('bmw', 240)

print(volvo + BMW)
