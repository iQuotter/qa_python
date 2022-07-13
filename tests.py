from main import BooksCollector


class TestBooksCollector:

    def test__init__books_rating_type_dict(self):
        books_collector = BooksCollector()

        assert type(books_collector.books_rating) == dict

    def test__init__books_favorites_type_list(self):
        books_collector = BooksCollector()

        assert type(books_collector.favorites) == list

    def test_add_new_book_true(self):
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')

        assert 'Зеленая миля' in books_collector.books_rating

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_base_rating1(self):
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')

        assert books_collector.books_rating['Зеленая миля'] == 1

    def test_add_new_book_twice_false(self):
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.add_new_book('Зеленая миля')
        books_collector.add_new_book('Зеленая миля')

        assert len(books_collector.books_rating) == 1

    def test_set_book_rating_for_a_non_existing_book(self):
        lower_rating = 5
        books_collector = BooksCollector()

        assert books_collector.set_book_rating('Зеленая миля', lower_rating) is None

    def test_set_book_rating_true(self):
        new_rating = 2
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.set_book_rating('Зеленая миля', new_rating)

        assert books_collector.books_rating['Зеленая миля'] != 1 \
               and books_collector.books_rating['Зеленая миля'] == new_rating

    def test_set_book_rating_lower_1(self):
        lower_rating = 0
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.set_book_rating('Зеленая миля', lower_rating)

        assert books_collector.books_rating['Зеленая миля'] != lower_rating

    def test_set_book_rating_1(self):
        lower_rating = 1
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.set_book_rating('Зеленая миля', lower_rating)

        assert books_collector.books_rating['Зеленая миля'] == lower_rating

    def test_set_book_rating_9(self):
        rating = 9
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.set_book_rating('Зеленая миля', rating)

        assert books_collector.books_rating['Зеленая миля'] == rating

    def test_set_book_rating_max_10(self):
        max_rating = 10
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.set_book_rating('Зеленая миля', max_rating)

        assert books_collector.books_rating['Зеленая миля'] == max_rating

    def test_set_book_rating_more_than_max(self):
        upper_rating = 11
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.set_book_rating('Зеленая миля', upper_rating)

        assert books_collector.books_rating['Зеленая миля'] != upper_rating

    def test_get_book_rating_true(self):
        rating = 7
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.set_book_rating('Зеленая миля', rating)

        assert books_collector.get_book_rating('Зеленая миля') == rating

    def test_get_books_rating_type(self):
        books_collector = BooksCollector()

        assert type(books_collector.get_books_rating()) == dict

    def test_get_books_rating_dict(self):
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.add_new_book('The Green Mile')

        assert books_collector.books_rating == books_collector.get_books_rating()

    def test_add_book_in_favorites_true(self):
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.add_book_in_favorites('Зеленая миля')

        assert 'Зеленая миля' in books_collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_for_a_non_existing_books_rating(self):
        books_collector = BooksCollector()

        assert books_collector.add_book_in_favorites('Зеленая миля') is None

    def test_delete_book_from_favorites_true(self):
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.add_book_in_favorites('Зеленая миля')
        books_collector.delete_book_from_favorites('Зеленая миля')

        assert 'Зеленая миля' not in books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_true(self):
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.add_book_in_favorites('Зеленая миля')

        assert books_collector.get_list_of_favorites_books()

    def test_get_books_with_specific_rating(self):
        rating = 5
        books_collector = BooksCollector()

        books_collector.add_new_book('Зеленая миля')
        books_collector.add_new_book('The Green Mile')
        books_collector.add_new_book('Yaşıl Mil')
        books_collector.add_new_book('አረንጓዴ ማይል')
        books_collector.add_new_book('Milje e Gjelbër')
        books_collector.add_new_book('Կանաչ մղոն')

        books_collector.set_book_rating('Зеленая миля', 10)
        books_collector.set_book_rating('The Green Mile', 6)
        books_collector.set_book_rating('Yaşıl Mil', 5)
        books_collector.set_book_rating('አረንጓዴ ማይል', 3)
        books_collector.set_book_rating('Milje e Gjelbër', 5)
        books_collector.set_book_rating('Կանաչ մղոն', 9)

        key_list_specific_rating = []
        for key, value in books_collector.books_rating.items():
            if value == rating:
                key_list_specific_rating.append(key)

        assert books_collector.get_books_with_specific_rating(rating) == key_list_specific_rating
