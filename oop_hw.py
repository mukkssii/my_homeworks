from datetime import datetime


class Transport:

    def __init__(self, brand, made_in, fuel_consumption, year=2020):
        self.made_in = made_in
        self.brand = brand
        self.year = year
        self.mileage = 0
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f'<Car> brand: {self.brand}, it was made in {self.made_in}, in {self.year}, and it needs {self.fuel_consumption} liters for 100 km'

    @property
    def car_age(self):
        age = (datetime.today().year - self.year)
        return age


car = Transport(brand='BMW', made_in='China', fuel_consumption=30.4)
car1 = Transport(brand='Hyundai', made_in='Czech Republic', fuel_consumption=40.8)
car2 = Transport(brand='Mercedes', made_in='Germany', fuel_consumption=38.2)
car3 = Transport(brand='Ford', made_in='UK', fuel_consumption=60.6)

print(car)
print(car.car_age)
print(car1)
print(car1.car_age)
print(car2)
print(car2.car_age)
print(car3)
print(car3.car_age)
