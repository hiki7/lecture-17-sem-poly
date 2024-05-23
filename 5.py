from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self, name, type, sound):
        self._name = name
        self._type = type
        self._sound = sound

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sound(self):
        pass

    @abstractmethod
    def play(self):
        pass


class StringedInstrument(Instrument):
    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_sound(self):
        return self._sound

    def play(self):
        return f"Звучит струнный инструмент {self._name}"


class PercussionInstrument(Instrument):
    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_sound(self):
        return self._sound

    def play(self):
        return f"Звучит ударный инструмент {self._name}"


class Orchestra:
    def __init__(self):
        self.instruments = []

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    def list_instruments(self):
        return [instro.get_name() for instro in self.instruments]

    def list_stringed_instruments(self):
        return [instro.get_name() for instro in self.instruments if isinstance(instro, StringedInstrument)]

    def list_percussion_instruments(self):
        return [instro.get_name() for instro in self.instruments if isinstance(instro, PercussionInstrument)]


chello = StringedInstrument("виолончель", "струнный инструмент", "Strum")
maracas = PercussionInstrument("маракасы", "ударный инструмент", "Maracas")
violin = StringedInstrument("скрипка", "струнный инструмент", "Virtuso")
drums = PercussionInstrument("барабан", "ударный инструмент", "Beat")

orchestra = Orchestra()
orchestra.add_instrument(chello)
orchestra.add_instrument(maracas)
orchestra.add_instrument(violin)
orchestra.add_instrument(drums)

print("В оркестрe есть инструменты:", ', '.join(orchestra.list_instruments()))
print("Струнные инструменты:", ', '.join(orchestra.list_stringed_instruments()))
print("Ударные инструменты:", ', '.join(orchestra.list_percussion_instruments()))

print(chello.play())
print(drums.play())