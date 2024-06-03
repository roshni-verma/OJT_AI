class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_battery_info(self):
        return f"Battery capacity: {self.battery_capacity} kWh"

# Example usage:
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_info())

my_electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
print(my_electric_car.display_info())
print(my_electric_car.display_battery_info())
