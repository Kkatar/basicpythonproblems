# 13.Python Object-Oriented Programming (OOP) Exercise: Classes and Objects Exercises

# OOP Exercise 1: Create a Class with instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

maruti = Vehicle(120, 15)
print(maruti.max_speed, maruti.mileage)


# OOP Exercise 2: Create a Vehicle class without any variables and methods
class Vehicle:
    pass


# OOP Exercise 3: How to Modify attributes in class
class Car():
    """A simple attempt to create a car"""
    def __init__(self, make, model, year):  # __init__: means this will run automatically
        """initialize car attribute"""
        self.make = make
        self.model = model
        self.year = year

        # fuel capacity and level in gallons
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """fill gas tank to capacity"""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full")

    def drive(self):
        """stimulate driving"""
        print("The car is moving")

# let create object of Car class
my_car = Car("Audi", "G3", 2022)

# accessing attribute values
print(my_car.make)
print(my_car.model)
print(my_car.year)

# calling methods
my_car.drive()
my_car.fill_tank()

# Modifying attributes
my_car.fuel_level = 5
print(my_car.fuel_level)

# Writing a method to update an attributes values
def update_fuel_level(self, new_level):
    """Update the fuel level"""
    if new_level <= self.fuel_capacity:
        self.fuel_level = new_level
    else:
        print("The tank can't hold that much")

# adding above function to original class as method from outside
Car.update_fuel_level = update_fuel_level
my_car.update_fuel_level(12)
print(my_car.fuel_level)

# Writing a method to increament an attributes values
def add_fuel(self, amount):
    """Add fuel to tank"""
    if (self.fuel_level + amount <= self.fuel_capacity):
        self.fuel_level += amount
        print("Added fuel")
    else:
        print("the tank cant hold that much")

Car.add_fuel = add_fuel
my_car.add_fuel(10)
my_car.add_fuel(2)
print(my_car.fuel_level)


# OOP Exercise 4: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus(70, 10)
print(School_bus.max_speed, School_bus.mileage)


# OOP Exercise 4: Class Inheritance
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def sitting_capacity(self, capacity):
        return f"sitting capacity of bus {self.name} is {capacity} passanger"

class Bus(Vehicle):
    # assign defualt value to capacity 50
    def sitting_capacity(self, capacity=50):
        return super().sitting_capacity(capacity=50)

School_bus = Bus("Volvo", 120, 23)
print(School_bus.sitting_capacity())


# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
class Vehicle:
    Color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("Volvo", 120, 23)
print(School_bus.name, School_bus.Color, School_bus.max_speed, School_bus.mileage)

Maruti = Car("Swift", 90, 41)
print(Maruti.name, Maruti.Color, Maruti.max_speed, Maruti.mileage)


# OOP Exercise 6: Class Inheritance
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 0.1
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


# OOP Exercise 7:Write a program to determine which class a given Bus object belongs to.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))
# so given object is belong to class bus


# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))
