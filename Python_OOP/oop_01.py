#Classes and Objects
#Class Creation
class Car:

    totalCar = 0  # To track The NO. of objects Are created we created this to measure the no. of car
    def __init__(self,__brand,model):
        self.__brand = __brand
        self.__model = __model
        Car.totalCar += 1 # to calculate how many times it is used to crate object

# Getter Methond For Controlled Output
    def get___brand(self):
        return self.__brand + "!!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol"
    
    @property
    def __model(self):
        return self.__model
    
    @staticmethod    # Decortors 
    def general_descript():
        return "My Car Is So Expensive.!!"

# Created Object Of The Car class
my_car = Car("Toyota", "Corolla")
'''print(my_car.__brand,my_car.__model)
print(my_car.full_name())'''
""""
my_another_car = Car("Tata","Harrier")
print(my_another_car.__brand,my_another_car.__model)"""

#Inheritance

class ElectricCar(Car):
    def __init__(self,__brand,__model,battery_size):
        super().__init__(__brand , __model)     # Gives Access to all of the Parent class formal parameters
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("tesla","Model S pro", "85kWh")
print(my_tesla.full_name())     # Thats How inheritance works...!!

# Encapsulation

# We have Encapsulated the getter method so we can get The controlled output by it..
#Output : tesla !!
# Add "__" For TO make private
"""
print(my_tesla.__brand)
print(my_tesla.get___brand)
"""
# Polymorphism 

safari = Car("tata", "safari")
safari3 = Car("tata", "Punch")
print(safari.fuel_type())  # Output is Petrol as it is the object of the Car Class Only

# Class Variable

print(safari.totalCar)
print(Car.totalCar)

# Static Method 
my_car = Car("Tata","Nexon")
print(my_car.general_descript())    
print(Car.general_descript())

# Property Decorator

my_car.__model = "city"
print(my_car.__model)

#To make read Only this Model

print(my_car.model)

#Class Inheritance And instance() function

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

# Multiple Inheritance

class Battery :
   def Battery_info(self):
       return "This Is Battery."
   
class Engine:
    def Engine_info(self):
        return "This Is Engine."

class ElectricCarTwo(Battery,Engine,Car):
    pass

myNewtesla = ElectricCarTwo("Tesla,"Model")
print(myNewtesla.Battery_info())