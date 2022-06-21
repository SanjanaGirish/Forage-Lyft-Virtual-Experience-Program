from Serviceable import Serviceable
from main.engines.engine import Engine
from main.Batteries import battery


class Car(Serviceable):
    """ A subclass of serviceable. Create a car with specific engine and
    battery. """
    engine: Engine
    battery: battery

    def __init__(self, engine, battery):
        super().__init__()
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        """ Method to check if the car needs service """
        return self.engine.needs_service() or self.battery.needs_service()
