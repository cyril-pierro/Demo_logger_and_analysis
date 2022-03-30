from demo.models.person import Person
from demo.models.store import Store

kofi = Person("kofi", "first")
store = Store(kofi)

product_message = "Enter product name "
price_message = "Enter amount of Product "

while True:
    result = input("command : ")
    if result.lower() == "add":
        product = input(product_message)
        value = input(price_message)
        store.add(product, int(value))
    elif result.lower() == "buy":
        product = input(product_message)
        value = input(price_message)
        store.buy(product, int(value))
    elif result.lower() == "sell":
        product = input(product_message)
        value = input(price_message)
        store.sell(product, int(value))
    elif result.lower() == "show":
        print(store.show_case)
