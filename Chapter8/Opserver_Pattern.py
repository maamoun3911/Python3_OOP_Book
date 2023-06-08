from typing import Any


class Inventory:
    def __init__(self) -> None:
        self.observers = []
        self._product = None
        self._quantity = 0
    
    def attach(self, observer):
        self.observers.append(observer)
    
    # @property
    def get_product(self):
        return self._product
    # @property.setter
    def set_product(self, value):
        self._product = value
        self.update_observe()
    
    # @property
    def get_quantity(self):
        return self._quantity
    # @property.setter
    def set_quantity(self, value):
        self._quantity = value
        self.update_observe()
    
    def update_observe(self):
        for observer in self.observers:
            observer()

    quantity = property(get_quantity, set_quantity)
    product = property(get_product, set_product)


class ConsoleObserver:
    def __init__(self, inventory: Inventory) -> None:
        self.inventory = inventory
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f"product: {self.inventory.product}, inventory: {self.inventory.quantity}")

i = Inventory()
c = ConsoleObserver(i)
i.attach(c)
i.product = "Widget"
i.quantity = 5
c1 = ConsoleObserver(i)
i.attach(c1)
c2 = ConsoleObserver(i)
i.attach(c2)
for j in i.observers:
    print(j())