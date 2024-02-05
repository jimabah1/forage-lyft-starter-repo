# concrete_capulet_engine.py
from datetime import datetime, timedelta
from car import Car  # Import the Car class or adjust as needed

class ConcreteCapuletEngine(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        # Service is needed if the mileage exceeds 30,000 or if it's been more than 2 years
        mileage_threshold = 30000
        time_threshold = timedelta(days=365 * 2)
        return (self.current_mileage - self.last_service_mileage > mileage_threshold) or \
               (datetime.today().date() - self.last_service_date > time_threshold)
