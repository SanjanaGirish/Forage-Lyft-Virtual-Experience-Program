from numpy import array


class CarriganTires:
    """ Carrigan tires should be serviced only when one or more of the
    values in the tire wear array is greater than or equal to 0.9 """
    tire_wear: array

    def __init__(self, tire_wear):
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self):
        """ Method to check if the tires needs service """
        for tire in self.tire_wear:
            if tire > 0.9:
                return True
        return False

