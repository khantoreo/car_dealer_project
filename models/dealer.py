from models.car import Car

class Dealership:
    def __init__(self, name: str):
        name = name
        self.name = name
        self.cars = []        
        self.sold_total = 0.0 

    def add_car(self, car: Car):
        self.cars.append(car)

    def remove_car(self, brand: str, model: str) -> bool:
        for car in self.cars:
            if car.brand.lower() == brand.lower() and car.model.lower() == model.lower():
                self.cars.remove(car)
                return True
        return False

    def sell_car(self, brand: str, model: str) -> bool:
        for car in self.cars:
            if car.brand.lower() == brand.lower() and car.model.lower() == model.lower():
                self.sold_total += car.price
                self.cars.remove(car)
                return True
        return False