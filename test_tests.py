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
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre


    # тестируем вывод списка книг с определённым жанром
    def test_get_books_with_specific_genre(self, collector):
        books_with_specific_genre = []
        genre = 'Фантастика'
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Дюна')
        collector.add_new_book('«Убийство в Восточном экспрессе')
        collector.add_new_book('Путеводитель автостопом по Галактике')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        collector.set_book_genre('Путеводитель автостопом по Галактике', 'Фантастика')
        
        for name, value in collector.books_genre.items():
            if value == genre:
                books_with_specific_genre.append(name)

        assert collector.get_books_with_specific_genre(genre) == books_with_specific_genre

    # тестируем вывод списка книг для детей
    def test_get_books_for_children(self, collector):
        books_for_children = []
        for name, genre in  collector.books_genre.items():
            if genre not in['Ужасы', 'Детективы']:
                books_for_children.append(name)
        assert  collector.get_books_for_children() == books_for_children


    # тестируем добавление книги в Избранное
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Властелин колец')
        name = 'Властелин колец'
        collector.add_book_in_favorites(name)
        assert collector.favorites == [name]


    # тестируем удаление книги из Избранного
    def test_delete_book_from_favorites(self, collector):
        name = 'Дюна'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()
        collector.favorites.remove(name)
        assert name not in collector.favorites


    # проверяем, что невозможно вевести список книг с жанром которого нет в списке self.genre
    def test_get_books_with_genre_that_is_not_on_the_list(self, collector):
        books_with_specific_genre = []
        name = 'Исчезнувшая'
        genre = 'Триллер'
        collector.books_genre[name] = genre
        assert collector.get_books_with_specific_genre(genre) == books_with_specific_genre


    # проверяем, что после добавления книги у неё нет жанра
    def test_books_without_specific_genre_after_add(self, collector):
        name = 'Этерна'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ""



    # проверяем, что невозможно установить книге жанр, которого нет в списке self.genre
    def test_set_book_genre(self, collector):
        genre = 'Исторический роман'
        name = 'Первый человек в Риме'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ""

        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == ""






if __name__ == "__main__":
    pytest.main()