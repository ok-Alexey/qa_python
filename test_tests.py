import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2
        

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    

    # тестируем add_genre_one_book - установка жанра для одной книги
    def test_set_book_genre_add_genre_one_book(self, collector):
        genre = 'Детективы'
        name = 'Что делать, если ваш кот хочет вас убить'
        collector.books_genre[name] = ""
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == 'Детективы' 


    # получаем жанр книги по её имени
    def test_get_book_genre_by_its_name(name, collector):
        name = 'Исчезнувшая'
        genre = 'Триллер'
        collector.books_genre[name] = genre
        assert collector.get_book_genre(name) == genre


    # тестируем вывод списка книг с определённым жанром
    def test_get_books_with_specific_genre(self, collector):
        books_with_specific_genre = []
        genre = 'Фантастика'
        collector.books_genre = {
        'Властелин колец' : 'Фантастика',
        'Дюна' : 'Фантастика',
        'Убийство в Восточном экспрессе' : 'Детективы',
        'Путеводитель автостопом по Галактике' : 'Фантастика'
        }
        for name, value in collector.books_genre.items():
            if value == genre:
                books_with_specific_genre.append(name)

        assert collector.get_books_with_specific_genre(genre) == books_with_specific_genre


        # получаем словарь books_genre 
    def test_get_books_genre(self, collector):
        name = 'Путеводитель автостопом по Галактике'
        genre = 'Фантастика'
        collector.books_genre[name] = genre
        assert collector.get_books_genre() == collector.books_genre

    # тестируем вывод списка книг для детей
    def test_get_books_for_children(self, collector):
        books_for_children = []
        collector.books_genre = {
        'Властелин колец' : 'Фантастика',
        'Дюна' : 'Фантастика',
        'Убийство в Восточном экспрессе' : 'Детективы',
        'Путеводитель автостопом по Галактике' : 'Фантастика'
        }
        for name, genre in  collector.books_genre.items():
            if genre not in['Ужасы', 'Детективы']:
                books_for_children.append(name)
        assert  collector.get_books_for_children() == books_for_children


    # тестируем добавление книги в Избранное 
    def test_add_book_in_favorites(self, collector):
        name = 'Властелин колец'
        collector.books_genre[name] = ""
        collector.add_book_in_favorites(name)
        assert collector.favorites == [name]


    # тестируем удаление книги из Избранного
    def test_delete_book_from_favorites(self, collector):
        name = 'Дюна'
        collector.favorites = [name]
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites 


    # получаем список Избранных книг 
    def test_get_list_of_favorites_books(self, collector):
        name = 'Путеводитель автостопом по Галактике'
        collector.favorites = [name]
        assert collector.get_list_of_favorites_books() == collector.favorites


if __name__ == "__main__":
    pytest.main()