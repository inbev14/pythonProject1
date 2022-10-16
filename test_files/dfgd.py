from collections import namedtuple

Car = namedtuple('cars', 'model miles')
cars = [
    Car('Toyota', 25000),
    Car('BMW', 43000),
    Car('Chery', 60000),
]

for car in cars:
    print(f"{car.model}")
    print(f"{car.miles}")
    
