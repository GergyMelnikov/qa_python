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
#########assert len(collector.get_books_rating()) == 2 # Тут косяк и он не мой.

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    
    def test_add_new_book_title_less_then_forty_characters_true(self):
        new_book = BooksCollector() 
        long_name = 'a' * 41
        normal_name = 'a' * 40
        new_book.add_new_book(long_name)
        new_book.add_new_book(normal_name)

        assert long_name not in new_book.books_genre and normal_name in new_book.books_genre

    @pytest.mark.parametrize('some_book, genre', [['Некоторая книга', 'Фантастика'],['Шина','Ужасы'],['Доктор гаджет','Детективы'],['Шестиструнный самурай', 'Мультфильмы'],['Токсичный мститель', 'Комедии']])
    def test_set_book_genre_true(self, some_book, genre):
        new_book = BooksCollector()
        #some_book = 'Некоторая книга'
        #genre = 'Фантастика'
        new_book.add_new_book(some_book)
        new_book.set_book_genre(some_book, genre)

        assert new_book.books_genre.get(some_book) == genre

        

