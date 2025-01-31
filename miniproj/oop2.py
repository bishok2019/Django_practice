from abc import ABC, abstractmethod

# ==== Decorator ====
# A decorator is a function that modifies the behavior of another function.
# Here, we create a decorator to log method calls.
def log_method_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__}")  # Log the method name
        result = func(*args, **kwargs)  # Execute the original method
        print(f"Method {func.__name__} executed successfully.")  # Log success
        return result
    return wrapper


# ==== Abstract Base Class ====
# Abstraction: Hides complex details and exposes only essential features.
class Car(ABC):
    car_count = 0  # Class variable (shared across all instances)

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = 0  # Private attribute (encapsulation)
        Car.car_count += 1  # Increment class variable

    # Abstract Method: Must be implemented by child classes.
    @abstractmethod
    def printDetails(self):
        pass

    # Concrete Method with Decorator
    @log_method_call  # Applying the decorator
    def accelerate(self):
        print("Speed up ...")

    @log_method_call  # Applying the decorator
    def break_applied(self):
        print("Car stopped")

    # Getter for private attribute (Encapsulation)
    def get_mileage(self):
        return self.__mileage

    # Setter for private attribute (Encapsulation)
    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            print("Mileage cannot be negative.")

    # Static Method: Does not depend on instance or class state.
    @staticmethod
    def is_vintage(year):
        return year < 2000

    # Class Method: Works with class variables.
    @classmethod
    def get_car_count(cls):
        return cls.car_count

    # Generator: Yields values lazily (one at a time).
    def mileage_history(self):
        current_mileage = 0
        while current_mileage < self.__mileage:
            yield current_mileage  # Yield the current mileage
            current_mileage += 1000  # Simulate mileage increments


# ==== Child Class: Hatchback ====
# Inheritance: Hatchback inherits from Car.
class Hatchback(Car):
    def printDetails(self):
        # Polymorphism: Each subclass provides its own implementation of printDetails.
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Not having this feature")


# ==== Child Class: SUV ====
# Inheritance: Suv inherits from Car.
class Suv(Car):
    def printDetails(self):
        # Polymorphism: Each subclass provides its own implementation of printDetails.
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Available")


# ==== Composition: Engine Class ====
# Composition: Building complex objects by combining simpler ones.
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f"{self.engine_type} engine started.")


# ==== Class Using Composition ====
class ElectricCar(Car):
    def __init__(self, brand, model, year, engine_type):
        super().__init__(brand, model, year)
        self.engine = Engine(engine_type)  # Composition: ElectricCar "has-a" Engine

    def printDetails(self):
        # Polymorphism: Each subclass provides its own implementation of printDetails.
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        self.engine.start()  # Using composed object


# ==== Method Overloading (Simulated) ====
# Python doesn't support method overloading directly, but we can simulate it using default arguments.
class Sedan(Car):
    def __init__(self, brand, model, year, fuel_type="Petrol"):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def printDetails(self):
        # Polymorphism: Each subclass provides its own implementation of printDetails.
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Fuel Type:", self.fuel_type)


# ==== Example Usage ====
if __name__ == "__main__":
    # Create instances
    car1 = Hatchback("Maruti", "Alto", "2022")
    car2 = Suv("Toyota", "Fortuner", "2023")
    car3 = ElectricCar("Tesla", "Model S", "2021", "Electric")
    car4 = Sedan("Honda", "City", "2020", "Diesel")

    # Polymorphism: Different objects treated as Car
    cars = [car1, car2, car3, car4]
    for car in cars:
        car.printDetails()  # Each car type implements printDetails differently
        print("------")

    # Decorator: Log method calls
    car1.accelerate()  # Logs method call
    car1.break_applied()  # Logs method call

    # Encapsulation: Getter and Setter
    car1.set_mileage(5000)
    print("Mileage:", car1.get_mileage())

    # Generator: Simulate mileage history
    print("Mileage History:")
    for mileage in car1.mileage_history():
        print(f"Current Mileage: {mileage} km")

    # Static Method
    print("Is vintage?", Car.is_vintage(1995))

    # Class Method
    print("Total cars created:", Car.get_car_count())