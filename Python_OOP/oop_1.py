"""
OOP in Python - Car Example

This script demonstrates:
1. Classes & Objects
2. Encapsulation (Private Attributes, Getter Methods, Property Decorators)
3. Inheritance & Method Overriding
4. Polymorphism
5. Class Variables & Static Methods
6. isinstance() function
7. Multiple Inheritance

Author: Atharva (Refactored with best practices)
"""

# -------------------------------
# CLASS CREATION
# -------------------------------
class Car:
    """
    Base class representing a generic Car.
    """

    total_cars = 0  # Class variable to track how many Car objects are created

    def __init__(self, brand: str, model: str):
        """
        Constructor for Car class.

        Args:
            brand (str): Car brand (e.g., Toyota, Tata)
            model (str): Car model (e.g., Corolla, Nexon)
        """
        self.__brand = brand          # Private attribute
        self.__model = model          # Private attribute
        Car.total_cars += 1           # Increment class counter when new object is created

    # Getter Method (Encapsulation: Controlled access to private attribute)
    def get_brand(self) -> str:
        return self.__brand + "!!"  # Controlled output

    # Normal method
    def full_name(self) -> str:
        return f"{self.__brand} {self.__model}"

    # Method to be overridden (Polymorphism)
    def fuel_type(self) -> str:
        return "Petrol"

    # Read-only property for model
    @property
    def model(self) -> str:
        return self.__model

    # Static method (belongs to class, not to any object)
    @staticmethod
    def general_description() -> str:
        return "Cars are expensive but useful vehicles!"


# -------------------------------
# INHERITANCE
# -------------------------------
class ElectricCar(Car):
    """
    Derived class representing an Electric Car.
    """

    def __init__(self, brand: str, model: str, battery_size: str):
        """
        Constructor for ElectricCar.

        Args:
            brand (str): Car brand
            model (str): Car model
            battery_size (str): Size of battery (e.g., 85kWh)
        """
        super().__init__(brand, model)   # Call parent constructor
        self.battery_size = battery_size

    # Overriding parent method (Polymorphism)
    def fuel_type(self) -> str:
        return "Electric Charge"


# -------------------------------
# MULTIPLE INHERITANCE
# -------------------------------
class Battery:
    def battery_info(self) -> str:
        return "This car has a powerful battery."


class Engine:
    def engine_info(self) -> str:
        return "This car has a strong engine."


class HybridCar(Battery, Engine, Car):
    """
    Demonstrates Multiple Inheritance.
    Inherits from Battery, Engine, and Car.
    """
    pass


# -------------------------------
# DRIVER CODE (TESTING)
# -------------------------------
if __name__ == "__main__":
    # Object creation
    my_car = Car("Toyota", "Corolla")
    print(my_car.full_name())          # Toyota Corolla
    print(my_car.get_brand())          # Toyota!!

    # Inheritance & Method Overriding
    my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
    print(my_tesla.full_name())        # Tesla Model S
    print(my_tesla.fuel_type())        # Electric Charge

    # Polymorphism
    safari = Car("Tata", "Safari")
    print(safari.fuel_type())          # Petrol (from parent class)

    # Class variable demonstration
    print("Total Cars Created:", Car.total_cars)

    # Static Method
    print(Car.general_description())
    print(my_car.general_description())

    # Property Decorator (Read-only attribute)
    print("Car Model:", my_car.model)

    # isinstance() demonstration
    print(isinstance(my_tesla, Car))         # True
    print(isinstance(my_tesla, ElectricCar)) # True

    # Multiple Inheritance Example
    my_hybrid = HybridCar("Honda", "Accord Hybrid")
    print(my_hybrid.full_name())        # Honda Accord Hybrid
    print(my_hybrid.battery_info())     # From Battery class
    print(my_hybrid.engine_info())      # From Engine class
