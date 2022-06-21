from datetime import date, datetime
from battery import Battery


class NubbinBatter(Battery):
    """ Subclass of Battery that should be serviced once every 2 years

    == ATTRIBUTES ==
    last_service_date: date of last service of battery
    current_date: current date
    """
    last_service_date: date
    current_date: date

    def __init__(self, last_service_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = datetime.today().date()

    def needs_service(self) -> bool:
        """ Method to check if the battery needs service """
        service_threshold_date = \
            self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < self.current_date
