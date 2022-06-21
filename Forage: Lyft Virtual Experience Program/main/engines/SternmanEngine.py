from engine import Engine


class SternmanEngine(Engine):
    """ A subclass of Engine. A sternman engine
    should be serviced only when the warning indicator is on

    == ATTRIBUTES ==
    warning_light_on: true if warning light is on
    """
    warning_light_on: bool

    def __init__(self, warning_light_on):
        super().__init__()
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        """ Method to check if the engine needs service """
        return self.warning_light_on
