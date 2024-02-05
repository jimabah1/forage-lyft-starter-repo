# concrete_willoughby_engine.py
from datetime import datetime, timedelta
from car import Car  # Import the Car class or adjust as needed

class ConcreteWilloughbyEngine(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        # Service is needed if the mileage exceeds 60,000
        mileage_threshold = 60000
        return self.current_mileage - self.last_service_mileage > mileage_threshold
