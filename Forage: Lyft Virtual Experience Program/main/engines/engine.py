class Engine:
    """ A superclass for all the engines.
    """

    def __init__(self):
        pass

    def needs_service(self) -> bool:
        """ Method to check if the engine needs service """
        raise NotImplementedError

