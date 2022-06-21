class Serviceable:
    """ Serviceable interface to check if cars need service """

    def needs_service(self) -> bool:
        """ Method to check if the engine needs service """
        raise NotImplementedError
