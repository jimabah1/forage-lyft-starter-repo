# car_model.py

# car_model.py
from datetime import datetime
from .serviceable import Serviceable
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

# Battery class definition
class Battery:
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # Common logic for all types of batteries
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < self.current_date

# SpindlerBattery class definition
class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)

    def needs_service(self):
        # Updated logic for SpindlerBattery
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return service_threshold_date <= self.current_date

        

# NubbinBattery class definition
class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)

    def needs_service(self):
        # Specific logic for NubbinBattery
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < self.current_date

# Tire class definition    
class CarriganTire:
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        # Carrigan tires need service if any value is greater than or equal to 0.9
        return any(wear >= 0.9 for wear in self.tire_wear_array)

class OctoprimeTire:
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        # Octoprime tires need service if the sum of all values is greater than or equal to 3
        return sum(self.tire_wear_array) >= 3

# Car model class definition
class Calliope(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()

class Glissade(WilloughbyEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()

class Palindrome(SternmanEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()

class Rorschach(WilloughbyEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()

class Thovex(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()

# Add other car models similarly

class CarModel(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    def some_method(self):
        # Example usage of Serviceable methods
        result = self.some_serviceable_method()
        # Additional implementation
        return result

    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)  # ADJUSTMENT: Use SpindlerBattery
        return CarModel(engine, battery)

    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)  # ADJUSTMENT: Use SpindlerBattery
        return CarModel(engine, battery)

    @staticmethod
    def create_palindrome(last_service_date, warning_light_is_on):
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = SpindlerBattery(last_service_date)  # ADJUSTMENT: Use SpindlerBattery
        return CarModel(engine, battery)

    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)  # ADJUSTMENT: Use NubbinBattery
        return CarModel(engine, battery)

    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)  # ADJUSTMENT: Use NubbinBattery
        return CarModel(engine, battery)

    # Add similar methods for other car models
