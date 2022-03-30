from abc import ABC, abstractmethod


class StoreI(ABC):
    """
    Store Interface class
    """

    @abstractmethod
    def sell(self, product_name: str, product_value: int):
        """
        Sell Product method
        """

    def buy(self, product_name: str, product_value: int):
        """
        Buy Product method
        """

    def add(self, product_name: str, product_value: int):
        """
        Add Product  method
        """
