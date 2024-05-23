from abc import ABC, abstractmethod
import random


class Movie(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def play(self):
        pass


class Horror(Movie):
    def play(self):
        print(f"Включаем фильм ужасов '{self.title}' реж. {self.author}.")


class Comedy(Movie):
    def play(self):
        print(f"Включаем комедию '{self.title}' реж. {self.author}.")


class Action(Movie):
    def play(self):
        print(f"Включаем боевик '{self.title}' реж. {self.author}.")


class Drama(Movie):
    def play(self):
        print(f"Включаем драму '{self.title}' реж. {self.author}.")


class Romance(Movie):
    def play(self):
        print(f"Включаем мелодраму '{self.title}' реж. {self.author}.")


class FilmCatalogue:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def play_all_movies(self):
        for movie in self.movies:
            movie.play()

    def play_movies_by_genre(self, genre):
        lst = [movie for movie in self.movies if isinstance(movie, genre)]
        random_movie = random.choice(lst)
        return random_movie.play()

    def search_movies_by_genre(self, genre):
        return [movie for movie in self.movies if isinstance(movie, genre)]


my_catalogue = FilmCatalogue()

my_catalogue.add_movie(Drama("Крестный отец", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Comedy("Ночные игры", "Джон Фрэнсис Дейли, Джонатан М. Голдштейн"))
my_catalogue.add_movie(Horror("Дракула Брэма Стокера", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Action("Крушение", "Жан-Франсуа Рише"))
my_catalogue.add_movie(Romance("Честная куртизанка", "Маршалл Херсковиц"))

my_catalogue.play_all_movies()

print(f"\nНайдены фильмы ужасов:")
for movie in my_catalogue.search_movies_by_genre(Horror):
    print(movie.title)

print(f"\nЗапускаем фильм из жанра 'Мелодрамы':")
my_catalogue.play_movies_by_genre(Romance)
