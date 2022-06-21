from numpy import array


class OctoprimeTires:
    """ Octoprime tires should be serviced only when the sum
    of all values in the tire wear array is greater than or equal to 3 """
    tire_wear: array

    def __init__(self, tire_wear):
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self):
        """ Method to check if the tires needs service """
        sum = 0
        for tire in self.tire_wear:
            sum += tire
        return sum >= 3
