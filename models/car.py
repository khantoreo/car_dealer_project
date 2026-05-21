class Car:
    def __init__(self, brand: str, model: str, price: float, mileage: float):
        self.brand = brand
        self.model = model
        self.__price = price      
        self.__mileage = mileage  
        self.is_electric = False

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = value

    @property
    def mileage(self) -> float:
        return self.__mileage

    @mileage.setter
    def mileage(self, value: float):
        if value < 0:
            raise ValueError("Mileage cannot be negative!")
        self.__mileage = value

    def get_details(self) -> str:
        return f"{self.brand} {self.model} | Mileage: {self.mileage} km | Price: ${self.price}"


class ElectricCar(Car):
    def __init__(self, brand: str, model: str, price: float, mileage: float, battery_capacity: int = 75):
        super().__init__(brand, model, price, mileage)
        self.is_electric = True
        self.battery_capacity = battery_capacity

    def get_details(self) -> str:
        base_details = super().get_details()
        return f"[⚡ EV] {base_details} | Battery: {self.battery_capacity} kWh"