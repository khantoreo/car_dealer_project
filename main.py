from models.dealer import Dealership
from models.car import Car, ElectricCar
from storage.file_handler import FileHandler
from utils.decorators import log_action
from utils.validators import Validator, car_generator
import sys

dealer = Dealership("Motors by Khantore & Nurali")

@log_action
def init_system():
    FileHandler.load_data(dealer)

@log_action
def add_car_ui():
    brand = input("Enter car brand: ").strip()
    model = input("Enter car model: ").strip()
    
    if not Validator.validate_brand_or_model(brand) or not Validator.validate_brand_or_model(model):
        print("❌ Invalid format! Only letters, numbers, spaces, and hyphens (2-20 characters).")
        return

    try:
        price = float(input("Enter price ($): "))
        mileage = float(input("Enter mileage (km): "))
        is_ev = input("Is it an Electric Vehicle? (yes/no): ").strip().lower() == 'yes'
        
        if is_ev:
            battery = int(input("Enter battery capacity (kWh): "))
            car = ElectricCar(brand, model, price, mileage, battery)
        else:
            car = Car(brand, model, price, mileage)
            
        dealer.add_car(car)
        FileHandler.save_data(dealer)
        print("🚗 Car added successfully!")
    except ValueError as e:
        print(f"❌ Invalid numeric input: {e}")

@log_action
def sell_car_ui():
    brand = input("Enter car brand to sell: ").strip()
    model = input("Enter car model to sell: ").strip()
    if dealer.sell_car(brand, model):
        FileHandler.save_data(dealer)
        print("💰 Car sold successfully!")
    else:
        print("❌ Car not found in stock!")

def show_cars():
    if not dealer.cars:
        print("The database is currently empty.")
        return
    print("\n=== AVAILABLE CARS IN STOCK ===")
    gen = car_generator(dealer.cars)
    for car in gen:
        print(car.get_details())
        
    ev_cars = list(filter(lambda c: c.is_electric, dealer.cars))
    print(f"\n💡 Total Electric Vehicles (EV): {len(ev_cars)}")

def main_menu():
    init_system()
    while True:
        print(f"\n--- {dealer.name} Menu ---")
        print("1. View available cars")
        print("2. Add a new car")
        print("3. Sell a car")
        print("4. View total revenue")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        if choice == "1":
            show_cars()
        elif choice == "2":
            add_car_ui()
        elif choice == "3":
            sell_car_ui()
        elif choice == "4":
            print(f"\n📊 Total revenue from all sales: ${dealer.sold_total}")
        elif choice == "5":
            FileHandler.save_data(dealer)
            print("Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main_menu()