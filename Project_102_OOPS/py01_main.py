
from py01_car import Car

my_car = Car()
print(my_car.make)  # Output: Toyota
print(my_car.year)  # Output: 2020

my_car.start_engine()  # Output: The Toyota Camry starts its engine.
my_car.drive()         # Output: The Toyota Camry drives forward.
my_car.stop_engine()   # Output: The Toyota Camry stops its engine.

#my_car = Car("Toyota", "Camry", 2020)