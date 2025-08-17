class Animal:

    def __init__(self, name) -> None:
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')


class Dog(Animal):
    def speak(self):
        print('Woof!')


class Cat(Animal):
    def speak(self):
        print('Meow!')


class Mouse(Animal):
    def speak(self):
        print('Squeek!')


dog = Dog('bruno')
cat = Cat('Tom')
mouse = Mouse('Jerry')


print(dog.name)
dog.speak()
print()
print(cat.name)
cat.speak()
print()
print(mouse.name)
mouse.speak()
print()
