from abc import ABC, abstractmethod

def print_run_tests(func):
    def wrapper(*args, **kwargs):
        print("Начинаем тест производительности...")
        func(*args, **kwargs)
        print("Тест производительности завершен.")
    return wrapper

class Computer(ABC):
    def __init__(self, model, processor, memory):
        self.model = model
        self.processor = processor
        self.memory = memory

    @abstractmethod
    def run(self):
        pass


class Desktop(Computer):
    @print_run_tests
    def run(self):
        print(f"Запускаем настольный компьютер '{self.model}' с процессором {self.processor} и {self.memory} RAM.")


class Laptop(Computer):
    @print_run_tests
    def run(self):
        print(f"Запускаем ноутбук '{self.model}' с процессором {self.processor} и {self.memory} RAM.")


class ComputerStore:
    def __init__(self):
        self.computers = []

    def add_computer(self, computer):
        self.computers.append(computer)

    def run_tests(self):
        for computer in self.computers:
            computer.run()


store = ComputerStore()
store.add_computer(Desktop("HP Legion", "Intel Core i9-10900K", "64 Гб"))
store.add_computer(Laptop("Dell Xtra", "Intel Core i5 13600K", "32 Гб"))
store.add_computer(Desktop("Lenovo SuperPad", "AMD Ryzen 7 2700X", "16 Гб"))
store.run_tests()