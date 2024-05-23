from abc import ABC, abstractmethod


class Dinosaur(ABC):
    def __init__(self, personal_name, breed, height, weight):
        self._personal_name = personal_name
        self._breed = breed
        self._height = height
        self._weight = weight

    @abstractmethod
    def get_personal_name(self):
        pass

    @abstractmethod
    def get_breed(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def get_diet(self):
        pass

    def get_info(self):
        return (self.get_personal_name(), self.get_breed(), self.get_weight(), self.get_height(), self.get_diet())


class Carnivore(Dinosaur):
    def __init__(self, personal_name, breed, height, weight):
        super().__init__(personal_name, breed, height, weight)
        self._diet = 'Плотоядный'

    def get_personal_name(self):
        return self._personal_name

    def get_breed(self):
        return self._breed

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weight

    def get_diet(self):
        return self._diet


class Herbivore(Dinosaur):
    def __init__(self, personal_name, breed, height, weight):
        super().__init__(personal_name, breed, height, weight)
        self._diet = 'Травоядный'

    def get_personal_name(self):
        return self._personal_name

    def get_breed(self):
        return self._breed

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weight

    def get_diet(self):
        return self._diet


class DinosaurPark:
    def __init__(self):
        self.dinosaurs = []

    def add_dinosaur(self, dinosaur):
        self.dinosaurs.append(dinosaur)

    def list_dinosaurs(self):
        return self.dinosaurs

    def list_carnivores(self):
        return [dino for dino in self.dinosaurs if isinstance(dino, Carnivore)]

    def list_herbivores(self):
        return [dino for dino in self.dinosaurs if isinstance(dino, Herbivore)]


t_rex = Carnivore('Тираннозавр', 'Рекс', 4800, 560)
velociraptor = Carnivore('Велоцираптор', 'Зубастик', 30, 70)
stegosaurus = Herbivore('Стегозавр', 'Стегга', 7100, 420)
triceratops = Herbivore('Трицератопс', 'Трипси', 8000, 290)

park = DinosaurPark()

park.add_dinosaur(t_rex)
park.add_dinosaur(velociraptor)
park.add_dinosaur(stegosaurus)
park.add_dinosaur(triceratops)


for dinosaur in park.list_dinosaurs():
    info = dinosaur.get_info()
    print(f'Имя: {info[0]}\n'
          f'Вид: {info[1]}\n'
          f'Вес: {info[2]} кг\n'
          f'Рост: {info[3]} см\n'
          f'Рацион: {info[4]}\n')
