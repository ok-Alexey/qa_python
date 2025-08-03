# qa_python
В проекте удалось реализовать следующие тесты:
def test_set_book_genre_add_genre_one_book - тестируем, что установка жанра для одной книги проходит успешно
def test_get_books_with_specific_genre - тестируем вывод списка книг с определённым жанром
def test_get_books_for_children - тестируем вывод списка книг для детей (в выводе не должно присутствовать фильмов с жанром не предназначенным для детей)
def test_add_book_in_favorites - тестируем, что добавление книги в Избранное проходит успешно
def test_delete_book_from_favorites - тестируем, что удаление книги из Избранного проходит успешно
def test_get_books_with_genre_that_is_not_on_the_list проверяем, что с помощью метода get_books_with_specific_genre() невозможно вевести список книг с жанром которого нет в списке self.genre
def test_books_without_specific_genre_after_add - проверяем, что после добавления книги у неё нет жанра
def test_set_book_genre - проверяем, что невозможно установить книге жанр, которого нет в списке self.genre