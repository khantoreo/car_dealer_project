import unittest
from models.car import Car, ElectricCar
from models.dealer import Dealership

class TestCarDealerSystem(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealership("Test Dealer")
        self.car1 = Car("Toyota", "Camry", 25000, 15000)
        self.car2 = ElectricCar("Tesla", "Model 3", 40000, 5000, 75)

    def test_add_car(self):
        self.dealer.add_car(self.car1)
        self.assertEqual(len(self.dealer.cars), 1)

    def test_electric_car_attributes(self):
        self.assertTrue(self.car2.is_electric)

    def test_sell_car_logic(self):
        self.dealer.add_car(self.car1)
        success = self.dealer.sell_car("Toyota", "Camry")
        self.assertTrue(success)
        self.assertEqual(self.dealer.sold_total, 25000)

    def test_invalid_price_set(self):
        with self.assertRaises(ValueError):
            self.car1.price = -1000

    def test_remove_nonexistent_car(self):
        success = self.dealer.remove_car("BMW", "X5")
        self.assertFalse(success)