from abc import ABC, abstractmethod


class Aircraft(ABC):
    def __init__(self, model, manufacturer, capacity):
        self.model = model
        self.manufacturer = manufacturer
        self.capacity = capacity

    @abstractmethod
    def fly(self):
        pass


class PassengerAircraft(Aircraft):
    def fly(self):
        print(f"Пассажирский самолет '{self.model}' вместимостью {self.capacity} человек, произведенный компанией {self.manufacturer}, "
              f"поднимается в воздух с пассажирами на борту.")


class CargoAircraft(Aircraft):
    def fly(self):
        print(f"Грузовой самолет '{self.model}' с грузоподъемностью {self.capacity} т, произведенный компанией {self.manufacturer}, "
              f"поднимается в воздух с грузом на борту.")


class Airport:
    def __init__(self):
        self.aircrafts = []

    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def takeoff(self):
        for aircraft in self.aircrafts:
            aircraft.fly()


airport = Airport()
airport.add_aircraft(PassengerAircraft("Boeing 747", "Боинг", 416))
airport.add_aircraft(CargoAircraft("Airbus A330", "Эйрбас", 70))
airport.add_aircraft(PassengerAircraft("Boeing 777", "Боинг", 396))
airport.takeoff()
