from abc import ABC, abstractmethod

class Ingredient(ABC):
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass


class Vegetable(Ingredient):
    def get_name(self):
        return self._name

    def get_quantity(self):
        return str(self._quantity) + " кг"


class Fruit(Ingredient):
    def get_name(self):
        return self._name

    def get_quantity(self):
        return str(self._quantity) + " кг"

carrot = Vegetable("Морковь", 5)
apple = Fruit("Яблоки", 10)

print(carrot.get_name())
print(carrot.get_quantity())

print(apple.get_name())
print(apple.get_quantity())
