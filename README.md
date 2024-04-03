# qa_python

1. test_add_new_book_add_two_books - проверяется количество книг, добавленных в словарь (Было в прекоде)
2. test_add_new_book_title_less_then_forty_characters_true - проверяет что нельзя добавить книгу с названием 41 символ и длиннее и можно добавить книгу с названием 40 символов и короче
3. test_set_book_genre_true - параматризованный тест, проверяет что соответствующий метод устанавливает жанр дял указанной книги
4. test_get_book_genre_true - параметризованный позитивный тест для геттера жанра по наименованию книги
5. test_get_books_with_specific_genre_true - позитивный тест метода для получения всех книг по жанру
6. test_get_books_genre_true - проверяет что метод отдающий словарь с книгами - отдает словарь с книгами
7. test_get_books_gor_children_true - проверяет что соответствующий метод отдает только книги с подходящими для детей жанрами(какими - указано в оригинальном методе)
8. test_add_book_in_favorites_true - проверяет что метод работает и добавляет книги в список избранных
9. test_delete_book_in_favorites_true - проверяет что мето работает и удаляет книги из списка избранных
10. test_get_list_of_favorites_books_empty_list - проверяет что метод может отдать пустой список