from abc import ABC, abstractmethod


class StoreI(ABC):
    """Store Interface"""

    @abstractmethod
    def sell(self, product_name: str, product_value: int):
        """Sell Product"""

    def buy(self, product_name: str, product_value: int):
        """Buy Product"""

    def add(self, product_name: str, product_value: int):
        """Add Product to Store"""
