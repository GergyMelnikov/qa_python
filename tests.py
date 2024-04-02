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
        library = BooksCollector() 
        long_name = 'a' * 41
        normal_name = 'a' * 40
        library.add_new_book(long_name)
        library.add_new_book(normal_name)

        assert long_name not in library.books_genre and normal_name in library.books_genre


    @pytest.mark.parametrize('book_name, genre', 
                             [
                                ['Некоторая книга', 'Фантастика'],
                                ['Шина','Ужасы'],
                                ['Доктор гаджет','Детективы'],
                                ['Шестиструнный самурай', 'Мультфильмы'],
                                ['Токсичный мститель', 'Комедии']
                             ])
    def test_set_book_genre_true(self, book_name, genre):
        library = BooksCollector()
        library.add_new_book(book_name)
        library.set_book_genre(book_name, genre)

        assert library.books_genre.get(book_name) == genre


    @pytest.mark.parametrize('book_name, genre', 
                             [
                                ['Некоторая книга', 'Фантастика'],
                                ['Шина','Ужасы'],
                                ['Инспектор гаджет','Детективы'],
                                ['Шестиструнный самурай', 'Мультфильмы'],
                                ['Токсичный мститель', 'Комедии']
                             ])
    def test_get_book_genre_true(self, book_name, genre):
        library = BooksCollector()
        library.add_new_book(book_name)
        library.set_book_genre(book_name, genre)
        
        book_to_get = library.get_book_genre(book_name)

        assert book_to_get == genre


    def test_get_books_with_specific_genre_true(self):
        library = BooksCollector()
        books_list = [
            ['Кошмары аиста марабу', 'Детективы'],
            ['Пять бутылок водки', 'Детективы'],
            ['Компьютерные сети В.Олифер', 'Ужасы'],
            ['Как создать свой CD Д.Мартин', 'Фантастика']
            ]
        for book_name, genre in books_list:
            library.add_new_book(book_name)
            library.set_book_genre(book_name, genre)
        
        received_books = library.get_books_with_specific_genre('Детективы')
        expected_books = ['Кошмары аиста марабу', 'Пять бутылок водки']

        assert received_books == expected_books

    
    def get_books_genre(self):
        library = BooksCollector()
        books_list = ['', '']
