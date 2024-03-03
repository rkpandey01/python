class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model} starts its engine.")

    def stop_engine(self):
        print(f"The {self.make} {self.model} stops its engine.")

    def drive(self):
        print(f"The {self.make} {self.model} drives forward.")