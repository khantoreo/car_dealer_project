import csv
import os
from models.car import Car, ElectricCar
from models.dealer import Dealership

class FileHandler:
    CSV_FILE = "data/cars_table.csv"
    TXT_FILE = "data/summary.txt"

    @staticmethod
    def ensure_data_dir():
        if not os.path.exists('data'):
            os.makedirs('data')

    @staticmethod
    def save_data(dealer: Dealership):
        FileHandler.ensure_data_dir()
        with open(FileHandler.CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Brand", "Model", "IsElectric", "Price", "Mileage"])
            for car in dealer.cars:
                writer.writerow([car.brand, car.model, car.is_electric, car.price, car.mileage])

        with open(FileHandler.TXT_FILE, mode='w', encoding='utf-8') as file:
            file.write(f"=== {dealer.name} DEALERSHIP REPORT ===\n")
            file.write(f"Current available cars in stock: {len(dealer.cars)}\n")
            file.write(f"Total revenue from sold cars: ${dealer.sold_total}\n")

    @staticmethod
    def load_data(dealer: Dealership):
        if not os.path.exists(FileHandler.CSV_FILE):
            return
        with open(FileHandler.CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                is_electric = row['IsElectric'] == 'True'
                if is_electric:
                    car = ElectricCar(row['Brand'], row['Model'], float(row['Price']), float(row['Mileage']))
                else:
                    car = Car(row['Brand'], row['Model'], float(row['Price']), float(row['Mileage']))
                dealer.add_car(car)
                
        if os.path.exists(FileHandler.TXT_FILE):
            with open(FileHandler.TXT_FILE, mode='r', encoding='utf-8') as file:
                for line in file:
                    if "Total revenue from sold cars:" in line:
                        try:
                            dealer.sold_total = float(line.split('$')[1].strip())
                        except:
                            dealer.sold_total = 0.0