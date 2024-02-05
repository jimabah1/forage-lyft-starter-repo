# concrete_sternman_engine.py
from car import Car  # Import the Car class or adjust as needed

class ConcreteSternmanEngine(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        # Service is needed if the warning light is on
        return self.warning_light_is_on
