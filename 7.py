from abc import ABC, abstractmethod


class Wine(ABC):
    def __init__(self, name, grape, year):
        self.name = name
        self.grape = grape
        self.year = year

    @abstractmethod
    def serve(self):
        pass


class RedWine(Wine):
    def serve(self):
        print(f"Красное вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, "
              f"рекомендуем подавать комнатной температуры.")


class WhiteWine(Wine):
    def serve(self):
        print(f"Белое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, "
              f"рекомендуем подавать хорошо охлажденным.")


class RoseWine(Wine):
    def serve(self):
        print(f"Розовое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, "
              f"рекомендуем подавать слегка охлажденным.")


class Winery:
    def __init__(self):
        self.wines = []

    def add_wine(self, wine):
        self.wines.append(wine)

    def serve_wines(self):
        for w in self.wines:
            w.serve()


winery = Winery()
winery.add_wine(RedWine("Cabernet Sauvignon", "Каберне Совиньон", 2015))
winery.add_wine(WhiteWine("Chardonnay", "Шардоне", 2018))
winery.add_wine(RoseWine("Grenache", "Гренаш", 2020))
winery.serve_wines()