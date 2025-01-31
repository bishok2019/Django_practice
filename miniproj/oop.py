# def log_method_call(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling method: {func.__name__}")  # Log the method name
#         result = func(*args, **kwargs)  # Call the original method
#         print(f"Method: {func.__name__} executed successfully.")  # Log success
#         return result
#     return wrapper
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model,fuel_type, color, noPlate):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        self.color = color
        self.__noPlate = noPlate

    @classmethod
    def create_default_vehicle(cls):
        # This method will create a default instance of the class it's called from
        return cls("Petrol", "Black","default123")

    @abstractmethod #abstraction
    def calculate_price(self): # Polymorphysm
        pass   

class Car(Vehicle): # Inherited properties of Vehicle
    def __init__(self, brand,model,fuel_type, color, noPlate):
        
        self.brand=brand
        self.model=model
        # self.vehicle = Vehicle(fuel_type, color) # since already inheriting from Vehicle
        self.fuel_type = fuel_type
        self.color = color
        self.__noPlate = noPlate # encapsulating by double underscore

     # Getter for noPlate
    def get_noPlate(self):
        return self.__noPlate

    # Setter for noPlate
    def set_noPlate(self, noPlate):
        self.__noPlate = noPlate
    
    def calculate_price(self):
        base_price = 20000
        if self.fuel_type == "Electric":
            return base_price + 10000
        else:
            return base_price
        
    def printDetails(self): # Instance method as it work on instance of object
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("color:",self.color)
        print("Fuel_type:",self.fuel_type)
        # print("Price: $", self.calculate_price())

#     # Generator to calculates price increase over time
#     @log_method_call
    def price_over_time(self, years, yearly_increase=10000):
        current_price = self.calculate_price()
        for year in range(1, years + 1):
            current_price += yearly_increase  # Increase price by a fixed amount
            yield current_price

#Create Car instance
# firstCar = Car('Tesla', 'T20','Petrol','Red','ABC123')
# print(firstcar.brand)
# print(firstcar.model)
# firstCar.printDetails()

# print("Car Number Plate:", firstCar.get_noPlate())

# print("\nCar Price Over Time:")
# for year, price in enumerate(firstCar.price_over_time(5), start=1):
#     print(f"Year {year}: ${price:.2f}")

##########################################################TRUCK####################################################
class Truck(Vehicle):
    def __init__(self, brand, model, fuel_type, color, wheel, noPlate):
        super().__init__(brand, model,fuel_type, color, noPlate)
        self.wheel=wheel
    # Getter for noPlate
    def get_noPlate(self):
        return self.__noPlate

    # Setter for noPlate
    def set_noPlate(self, noPlate):
        self.__noPlate = noPlate
 
    def calculate_price(self):
        # calculation by: base price + wheel bonus
        base_price = 50000
        wheel_bonus = self.wheel * 1000  # $1000 per wheel
        return base_price + wheel_bonus
    
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Fuel Type:", self.fuel_type)
        print("Wheels:", self.wheel)
        print("Number Plate:", self.get_noPlate())
        # print("Price: $", self.calculate_price())

# firstTruck = Truck('Tata', 'T21','Green','Diesel',16, 'XYZ123')
# print('Car Number Plate', firstCar._Car__noPlate)

# # print('Wheel: ',firstTruck.wheel)
# firstTruck.printVehicleDetails()
# # print("Truck Number Plate:", firstTruck.get_noPlate())

##########################################################BIKE####################################################

class Bike(Vehicle):
    def __init__(self, brand, model, fuel_type, color, engine_size, noPlate):
        super().__init__(brand, model,fuel_type, color, noPlate)
        # self.vehicle = Vehicle(fuel_type, color)
        self.engine_size = engine_size

    def calculate_price(self):
        base_price = 10000
        if self.fuel_type == "Electric":
            return base_price + 5000  # Add $5000 for Electric bikes
        else:
            return base_price + (self.engine_size * 10)  # Add $10 per cc for petrol bikes

    def printDetails(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Engine Size: {self.engine_size} cc")
        # print(f"Price: ${self.calculate_price()}")
firstBike = Bike('Harley', 'Sportster','Electric', 'Red', 1200)  # Engine size in cc

vehicles = [firstBike]

# Polymorphism in action: We call calculate_price on both, despite of being different logic for each
for vehicle in vehicles:
    print(f"The price of {vehicle.__class__.__name__} is ${vehicle.calculate_price()}\n")
    vehicle.printDetails()
# #  MRO Method Resolution Order
# class A():
#     def hello(self):
#         return f'hello !'
# class B():
#     def hello(self):
#         return f'Hi !'
# class C(A,B):
#     pass
#     # def hello(self):
#     #     return f'Bye !'
# a=C()
# print(a.hello())