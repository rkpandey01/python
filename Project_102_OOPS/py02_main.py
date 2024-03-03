from py02_Inheritance import Car

my_car = Car("Toyota", "Camry", 2020, 4)
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry
print(my_car.year)   # Output: 2020
print(my_car.doors)  # Output: 4
my_car.start_engine()  # Output: Engine started.
my_car.drive()         # Output: Car is driving.
my_car.stop_engine()   # Output: Engine stopped.
