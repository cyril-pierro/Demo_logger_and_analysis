from demo.interface.storeInterface import StoreI
from .person import Person
from typing import Dict
from .logger import Log
from demo import setting
plogger = Log(__name__, "debug", setting.logfile)


def error_decorator(function):
    """
    Wrapper for Error Messages
    @param function: Takes in a the function to decorate
    :return function
    """
    def inner(*args, **kwargs):

        # default message for Exception errors
        not_found = "Product {} not found"
        try:
            function(*args, **kwargs)
        except Exception as e:

            print(not_found.format(args[1]), e)
            plogger.error(not_found.format(args[1]))
    return inner


class Store(StoreI):
    """
    Store Class Structure
    """

    # Storage of all products stored by a user
    __products: Dict = {}

    def __init__(self, person: Person, product_name: str = None, product_amount: int = None):
        """
        Constructor for Store
        @param person: Object
        @param product_name: str
        @param product_amount: int
        :return None
        """
        # Required parameter when creating a Store
        self.person = person

        # Custom Validation
        if product_name is not None and product_amount is not None:
            self.__products[product_name] = product_amount

            plogger.info(
                f"Product Created - Name: {product_name} Value: {product_amount}")

    @error_decorator
    def buy(self, product_name: str, amount: int):
        """
        Buy method addes an amount to a product store
        @param product_name:str 
        @param amount: int
        :return None
        """

        value = self.__products.get(product_name)
        self.__products[product_name] = value + amount

        plogger.info(
            f"Product {product_name} bought by {self.person.first} on ")

    @error_decorator
    def sell(self, product_name: str, amount: int):
        """
        Sell method subtracts an amount from a product store
        @param product_name: str
        @param amount: int
        :return None
        """
        value = self.__products.get(product_name)
        self.__products[product_name] = value - amount
        plogger.info(f"Product {product_name} sold to {self.person.first} on ")

    def get_product_value(self, product_name: str):
        """
        Get Product Value method returns an amount of a product name
        @param product_name: 
        :return Integer
        """
        return self.__products.get(product_name)

    def add(self, product_name: str, product_amount: int):
        """
        Add method addes a new Product details to store
        @param product_name: str
        @param amount: int
        :return None
        """
        if product_name not in self.__products:
            plogger.info(f"New Product {product_name} added to inventory")
            self.__products[product_name] = product_amount
        else:
            plogger.error(f"Product {product_name} already exists")
            raise ValueError(f"Product {product_name} already exists")

    @property
    def show_case(self):
        """
        Show case method displays the available products in store
        @param product_name: str
        @param amount: str
        :return None
        """
        return self.__products
