# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"{self.brand} {self.model}'s engine started."

    def vehicle_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"

# Derived classes (Inheritance)
class Car(Vehicle):
    def start_engine(self):  # Polymorphism (method overriding)
        return f"{self.brand} {self.model} car engine roars to life!"

class Bus(Vehicle):
    def start_engine(self):  # Polymorphism
        return f"{self.brand} {self.model} bus engine rumbles loudly!"

class Bike(Vehicle):
    def start_engine(self):  # Polymorphism
        return f"{self.brand} {self.model} bike engine starts with a vroom!"

# Using Polymorphism
vehicles = [
    Car("Tesla", "Model S"),
    Bus("Volvo", "B9R"),
    Bike("Yamaha", "R15")
]

for v in vehicles:
    print(v.start_engine())  # Each object behaves differently
