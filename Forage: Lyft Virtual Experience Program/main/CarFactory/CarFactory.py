from datetime import date

from main.Batteries import NubbinBattery
from main.Batteries.SpindlerBattery import SpindlerBattery
from main.Cars.car import Car
from main.engines.CapuletEngine import CapuletEngine
from main.engines.SternmanEngine import SternmanEngine
from main.engines.WilloughbyEngine import WilloughbyEngine


class CarFactory:
    """ Cars are created by calling the corresponding create
    method on CarFactory """

    def create_calliope(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        """ Create calliope car with Capulet Engine and Spindler Battery"""
        return Car(engine=CapuletEngine, battery=SpindlerBattery)

    def create_glissade(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        """ Create glissade car with Willoughby Engine and Spindler Battery """
        return Car(engine=WilloughbyEngine, battery=SpindlerBattery)

    def create_palindrome(self, current_date: date, last_service_date: date,
                          warning_light_on: bool) -> Car:
        """ Create palindrome car with Sternman Engine and Spindler Battery"""
        return Car(engine=SternmanEngine, battery=SpindlerBattery)

    def create_rorschach(self, current_date: date, last_service_date: date,
                         current_mileage: int, last_service_mileage: int) -> Car:
        """ Create rorschach car with Willoughby Engine and Nubbin Battery """
        return Car(engine=WilloughbyEngine, battery=NubbinBattery)

    def create_thovex(self, current_date: date, last_service_date: date,
                      current_mileage: int, last_service_mileage: int) -> Car:
        """ Create thovex car with Capulet Engine and Nubbin Battery """
        return Car(engine=CapuletEngine, battery=NubbinBattery)
