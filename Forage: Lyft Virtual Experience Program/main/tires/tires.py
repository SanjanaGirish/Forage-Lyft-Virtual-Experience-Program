class Tires:
    """ Tires superclass for all types of tires """

    def __init__(self):
        pass

    def needs_service(self):
        """ Method to check if the tires needs service """
        raise NotImplementedError
