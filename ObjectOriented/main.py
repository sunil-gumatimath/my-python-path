from car import Car

car_1 = Car('chevy', 'corvette', 2021, 'red')
car_2 = Car('Ford', 'mustang', 2022, 'black')


print(car_1.model)
print(car_1.make)
print(car_1.color)
print(car_1.year)

car_1.drive()
car_1.stop()

print(car_2.model)
print(car_2.make)
print(car_2.color)
print(car_2.year)

car_2.drive()
car_2.stop()
