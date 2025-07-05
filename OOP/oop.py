class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand        

    def full_name(self):
        return f"{self.brand} {self.model}"

    def full_type(self):
        return "Petrol or Diesel"

    @staticmethod           
    def general_description():
        return "Cars are means of transport"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def full_type(self):
        return "Electric Charge"


# Object creation and usage
my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
print(my_tesla.full_name())                 # Tesla Model S
print(Car.general_description())            # Cars are means of transport

my_car = Car("Toyota", "Corolla")
print(my_car.brand)                         # Toyota
print(my_car.model)                         # Corolla
print(my_car.full_name())                   # Toyota Corolla

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)                     # Tata
print(my_new_car.model)                     # Safari

print(isinstance(my_tesla, Car))            # True
print(isinstance(my_tesla, ElectricCar))    # True


# Multiple inheritance example
class Battery:
    def battery_info(self):
        return "This is a battery"

class Engine:
    def engine_info(self):
        return "This is an engine"

class ElectricCarTwo(Battery, Engine, Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())           # This is an engine
print(my_new_tesla.battery_info())          # This is a battery
