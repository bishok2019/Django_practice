from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model,fuel_type, color, noPlate):
        self.brand = brand
        self.model = model
        self.fuel_type = self.validate_fuel_type(fuel_type)
        self.color = color
        self.__noPlate = noPlate
        # self.engine_size = engine_size

    @classmethod
    def create_vehicle(cls, brand=None, model=None, fuel_type=None, color=None, noPlate=None,engine_size=None):
        
        if brand is None:
            brand = "DefaultBrand"
        if model is None:
            model = "DefaultModel"
        if fuel_type is None:
            fuel_type = "Petrol"
        if color is None:
            color = "Black"
        if noPlate is None:
            noPlate = "default123"

        return cls(brand, model, fuel_type, color, noPlate, engine_size)
    @abstractmethod #abstraction
    def calculate_price(self): # Polymorphysm
        pass   

    @staticmethod
    def validate_fuel_type(fuel_type):
        allowed_types = {"Petrol", "Diesel", "Electric"}
        if fuel_type not in allowed_types:
            raise ValueError(f"Invalid fuel type: {fuel_type}. Allowed types are {allowed_types}.")
        return fuel_type

    @staticmethod
    def print_details(vehicle):
        """Static method to print vehicle details."""
        print(f"Brand: {vehicle.brand}")
        print(f"Model: {vehicle.model}")
        print(f"Color: {vehicle.color}")
        print(f"Fuel Type: {vehicle.fuel_type}")
        if hasattr(vehicle, "engine_size"):
            print(f"Number Plate: {vehicle._Vehicle__noPlate}") 
            print(f"Engine Size: {vehicle.engine_size} cc")
        print(f"Total Price: ${vehicle.calculate_price()}")
class Bike(Vehicle):
    def __init__(self, brand, model, fuel_type, color, noPlate, engine_size):
        super().__init__(brand, model,fuel_type, color, noPlate)
        self.engine_size = int(engine_size)

    def calculate_price(self):
        base_price = 1000
        if self.fuel_type == "Electric":
            return base_price + 5000  # Add $5000 for Electric bikes
        else:
            return base_price + (self.engine_size * 10)  # Add $10 per cc for petrol bikes

    # def printDetails(self):
    #     print(f"Brand: {self.brand}")
    #     print(f"Model: {self.model}")
    #     print(f"Color: {self.color}")
    #     print(f"Fuel Type: {self.fuel_type}")
    #     print(f"Engine Size: {self.engine_size} cc")
    #     print(f"Price: ${self.calculate_price()}")
# try:
#     # firstBike = Bike('Harley', 'Sportster','Electric', 'Red', engine_size=1200)  # this will git Bike class so it will throw error :TypeError: Bike.__init__() missing  required positional argument: 'noPlate' as noPlate is missing
#     firstBike = Bike.create_vehicle(brand = 'Harley', engine_size =250,fuel_type='Petrol')

#     print(f"The price of {firstBike.__class__.__name__} is ${firstBike.calculate_price()}\n")
#     # Bike.printDetails(firstBike)
#     Vehicle.print_details(firstBike)
# except ValueError as e:
#     print(e)

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
            
# firstBike = Bike.create_vehicle(brand = 'Harley', engine_size =250)
try:
    firstCar = Car('Tesla', 'T20','Petrol','Red','ABC123')
    Vehicle.print_details(firstCar)
    # print("\nCar Price Over Time:")
    # for year, price in enumerate(firstCar.price_over_time(4), start=1):
    #     print(f"Year {year}: ${price:.2f}")
except ValueError as e:
    print(e)