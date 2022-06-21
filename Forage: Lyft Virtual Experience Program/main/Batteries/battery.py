class Battery:
    """ A superclass for all batteries
    """

    def __init__(self):
        pass

    def needs_service(self) -> bool:
        """ Method to check if the battery needs service """
        raise NotImplementedError
