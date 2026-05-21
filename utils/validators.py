import re

class Validator:
    @staticmethod
    def validate_brand_or_model(text: str) -> bool:
        pattern = r"^[A-Za-z0-9\s\-]{2,20}$"
        return bool(re.match(pattern, text))

def car_generator(cars_list):
    for car in cars_list:
        yield car