from abc import ABC, abstractmethod


class PersonI(ABC):
    """
    Person Interface class
    """

    @abstractmethod
    def display(self):
        """
        Display Name method
        """
