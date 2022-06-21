from engine import Engine


class WilloughbyEngine(Engine):
    """ A subclass of Engine. A Willoughby engine
    should be serviced once every 60,000 miles

    == ATTRIBUTES ==
    current_mileage: number of current miles
    last_service_mileage: number of miles when last serviced
    """
    current_mileage: int
    last_service_mileage: int

    def __init__(self, current_mileage, last_service_mileage):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        """ Method to check if the engine needs service """
        return self.current_mileage - self.last_service_mileage > 60000
