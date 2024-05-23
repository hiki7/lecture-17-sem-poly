from abc import ABC, abstractmethod

def validatesoldier(method):
    def wrapper(self, *args, **kwargs):
        if not isinstance(self, Soldier):
            raise TypeError("It is not an instance of Soldier")
        return method(self, *args, **kwargs)
    return wrapper


class Soldier(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass


class Infantry(Soldier):
    @validatesoldier
    def move(self):
        print("Пехота передвигается в пешем порядке")

    @validatesoldier
    def attack(self):
        print("Пехота участвует в ближнем бою")

    @validatesoldier
    def defend(self):
        print("Пехота держит строй")


class Cavalry(Soldier):
    @validatesoldier
    def move(self):
        print("Кавалерия передвигается верхом")

    @validatesoldier
    def attack(self):
        print("Кавалерия переходит в атаку")

    @validatesoldier
    def defend(self):
        print("Кавалерия защищает фланги")


class Army:
    def __init__(self):
        self.soldiers = []

    def add_soldier(self, soldier):
        self.soldiers.append(soldier)

    def attack(self):
        for soldier in self.soldiers:
            soldier.move()
            soldier.attack()

    def defend(self):
        for soldier in self.soldiers:
            soldier.move()
            soldier.defend()


army = Army()
army.add_soldier(Infantry())
army.add_soldier(Cavalry())
army.add_soldier(Infantry())
army.add_soldier(Cavalry())

army.attack()
army.defend()
