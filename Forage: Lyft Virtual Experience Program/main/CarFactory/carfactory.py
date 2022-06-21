from datetime import date

from Batteries.NubbinBattery import NubbinBattery
from Batteries.SpindlerBattery import SpindlerBattery
from Cars.car import Car
from engines.CapuletEngine import CapuletEngine
from engines.SternmanEngine import SternmanEngine
from engines.WilloughbyEngine import WilloughbyEngine


class CarFactory:
    """ Cars are created by calling the corresponding create
    method on CarFactory """

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        """ Create calliope car with Capulet Engine and Spindler Battery"""
        engine = CapuletEngine(current_mileage=current_mileage,
                               last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(current_date=current_date,
                                  last_service_date=last_service_date)
        new_car = Car(engine=engine, battery=battery)
        return new_car

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        """ Create glissade car with Willoughby Engine and Spindler Battery """
        engine = WilloughbyEngine(current_mileage=current_mileage,
                                  last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(current_date=current_date,
                                  last_service_date=last_service_date)
        new_car = Car(engine=engine, battery=battery)
        return new_car

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date,
                          warning_light_on: bool) -> Car:
        """ Create palindrome car with Sternman Engine and Spindler Battery"""
        engine = SternmanEngine(warning_light_on=warning_light_on)
        battery = SpindlerBattery(current_date=current_date,
                                  last_service_date=last_service_date)
        new_car = Car(engine=engine, battery=battery)
        return new_car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date,
                         current_mileage: int,
                         last_service_mileage: int) -> Car:
        """ Create rorschach car with Willoughby Engine and Nubbin Battery """
        engine = WilloughbyEngine(current_mileage=current_mileage,
                                  last_service_mileage=last_service_mileage)
        battery = NubbinBattery(current_date=current_date,
                                last_service_date=last_service_date)
        new_car = Car(engine=engine, battery=battery)
        return new_car

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date,
                      current_mileage: int, last_service_mileage: int) -> Car:
        """ Create thovex car with Capulet Engine and Nubbin Battery """
        engine = CapuletEngine(current_mileage=current_mileage,
                               last_service_mileage=last_service_mileage)
        battery = NubbinBattery(current_date=current_date,
                                last_service_date=last_service_date)
        new_car = Car(engine=engine, battery=battery)
        return new_car
