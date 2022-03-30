from demo.interface.personInterface import PersonI
from demo.models.logger import Log
from demo import setting

# create a logger for Person object
plogger = Log(__name__, "info", setting.logfile)


class Person(PersonI):
    """
    Person Class
    """

    def __init__(self, first: str, second: str = ""):
        """
        @param first: str
        @param second: str
        :return None
        """
        self.first = first
        self.second = second
        plogger.info(f"Created Person: {self.display} - {self.email} at ")

    @property
    def email(self):
        """
        Email structure for Person Class
        """
        return f"{self.first}.{self.second}@email.com"

    @property
    def display(self):
        """
        Structure to display Person Class
        """
        return f"{self.first} {self.second}"
