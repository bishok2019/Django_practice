# class Solution:
#     def intToRoman(self, num):
#         val = [
#             (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
#             (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
#             (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
#             (1, 'I')
#         ]
        
#         # Generator for producing Roman numerals
#         for i, r in val:
#             while num >= i:
#                 yield r  # Yield each Roman numeral one at a time
#                 print(r)
#                 num -= i

# # Using the generator
# n = int(input("Enter an integer: "))
# solution = Solution()
# roman_numeral_gen = solution.intToRoman(n)
# roman_numeral = ''.join([char for char in roman_numeral_gen])  # Join the generator values into a string
# print(roman_numeral)



# Import required modules
from abc import ABC, abstractmethod

# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Create abstract method      
    @abstractmethod
    def printDetails(self):
        pass
  
    # Create concrete method
    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Car stopped")

# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Available")

# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")

# Call methods
car1.printDetails()
car1.accelerate()
car1.sunroof()