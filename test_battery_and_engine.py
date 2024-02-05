# In test_battery_and_engine.py

from datetime import date, timedelta
import unittest
from engine.model.car_model import SpindlerBattery
import unittest
from engine.model.car_model import CarriganTire, OctoprimeTire
from dateutil.relativedelta import relativedelta


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_after_three_years(self):
        # Arrange
        last_service_date = date.today() - relativedelta(years=3)
        current_date = date.today()
        battery = SpindlerBattery(last_service_date, current_date)

        # Act & Assert
        self.assertTrue(battery.needs_service())

class TestTireServicing(unittest.TestCase):
    def test_carrigan_tire_needs_service(self):
        # Arrange
        tire_wear_array = [0.8, 0.9, 0.85, 0.88]  # One value is greater than or equal to 0.9
        tire = CarriganTire(tire_wear_array)

        # Act & Assert
        self.assertTrue(tire.needs_service())

    def test_octoprime_tire_needs_service(self):
        # Arrange
        tire_wear_array = [0.8, 0.9, 0.85, 0.88]  # Sum is greater than or equal to 3
        tire = OctoprimeTire(tire_wear_array)

        # Act & Assert
        self.assertTrue(tire.needs_service())
