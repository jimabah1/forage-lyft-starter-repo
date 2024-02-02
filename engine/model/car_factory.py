# car_factory.py
from .car_model import CarModel

class CarFactory:
    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        return CarModel.create_calliope(last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        return CarModel.create_glissade(last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_palindrome(last_service_date, warning_light_is_on):
        return CarModel.create_palindrome(last_service_date, warning_light_is_on)

    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        return CarModel.create_rorschach(last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage):
        return CarModel.create_thovex(last_service_date, current_mileage, last_service_mileage)

    # Add similar methods for other car models
