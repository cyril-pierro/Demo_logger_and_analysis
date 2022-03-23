from abc import ABC, abstractmethod


class PersonI(ABC):
    """Person Interface"""

    @abstractmethod
    def display(self):
        """Display Name"""
