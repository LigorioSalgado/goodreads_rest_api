from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Book
from ..Authors.models import Author
from .serializers import BookSeriallizer

import datetime as dt
import json


class BooksTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.author_1 = Author.objects.create(
            name='test_name_1',
            last_name="test",
            nacionalidad="MX",
            biography="xsdasdasd",
            gender="M",
            age=45,
            is_alive=True

        )
        self.book1 = Book.objects.create(
            title='Book_test_name',
            author=self.author_1,
            isbn='12345678',
            date_published=dt.datetime.now(),
            raiting=4.5,
            cover="sasdasdas",
            prologue="asdasdas",
            literary_genre="DR",
            price=12.5
        )

    def test_get_all_books(self):
        response = self.client.get(reverse('books:list_books'))
        books = Book.objects.all()
        serializer = BookSeriallizer(books, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)


class CreateNewBookTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.author_1 = Author.objects.create(
            name='test_name_1',
            last_name="test",
            nacionalidad="MX",
            biography="xsdasdasd",
            gender="M",
            age=45,
            is_alive=True

        )
        self.valid_book = {
            'title': "Book new name",
            "author": self.author_1.id,
            "isbn": "wsadwqwqdqd",
            "date_published": '1999-01-01',
            "raiting": 4.5,
            "cover": "http://www.google.com/",
            "prologue": "adsadadasd",
            "literary_genre": "DR",
            "price": 12.5
        }

        self.invalid_book = {
            'title': "Book new name 2",
            "author": 1,
            "isbn": 23132423534,
            "date_published": "10/02/12",
            "raiting": 4,
            "cover": "sasdsadasd",
            "prologue": 2133432423,
            "literary_genre": "XC",
            "price": 12.1232342342422423
        }

    def test_create_valid_book(self):
        response = self.client.post(reverse('books:list_books'),
                                    data=json.dumps(self.valid_book),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_book(self):
        response = self.client.post(reverse('books:list_books'),
                                    data=json.dumps(self.invalid_book),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SingleBooksTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.author_1 = Author.objects.create(
            name='test_name_1',
            last_name="test",
            nacionalidad="MX",
            biography="xsdasdasd",
            gender="M",
            age=45,
            is_alive=True

        )
        self.book1 = Book.objects.create(
            title='Book_test_name',
            author=self.author_1,
            isbn='12345678',
            date_published=dt.datetime.now(),
            raiting=4.5,
            cover="sasdasdas",
            prologue="asdasdas",
            literary_genre="DR",
            price=12.5
        )
        self.book2 = Book.objects.create(
            title='Book_test_name 2',
            author=self.author_1,
            isbn='08765432',
            date_published=dt.datetime.now(),
            raiting=4.5,
            cover="sasdasdas",
            prologue="asdasdas",
            literary_genre="DR",
            price=13.5
        )

    def test_get_valid_single_book(self):
        response = self.client.get(
            reverse('books:details_book', kwargs={'pk': self.book1.id}))
        book = Book.objects.get(id=self.book1.id)
        serializer = BookSeriallizer(book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    def test_get_invalid_single_book(self):
        response = self.client.get(
            reverse('books:details_book', kwargs={'pk': 100}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateBookTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.author_1 = Author.objects.create(
            name='test_name_1',
            last_name="test",
            nacionalidad="MX",
            biography="xsdasdasd",
            gender="M",
            age=45,
            is_alive=True

        )
        self.book1 = Book.objects.create(
            title='Book_test_name',
            author=self.author_1,
            isbn='12345678',
            date_published=dt.datetime.now(),
            raiting=4.5,
            cover="sasdasdas",
            prologue="asdasdas",
            literary_genre="DR",
            price=12.5
        )
        self.book2 = Book.objects.create(
            title='Book_test_name 2',
            author=self.author_1,
            isbn='08765432',
            date_published=dt.datetime.now(),
            raiting=4.5,
            cover="sasdasdas",
            prologue="asdasdas",
            literary_genre="DR",
            price=13.5
        )
        self.valid_book = {
            'title': "Book_test_name",
            "author": self.author_1.id,
            "isbn": "12345678",
            "date_published": '1999-01-01',
            "raiting": 4.5,
            "cover": "http://www.google.com/",
            "prologue": "adsadadasd",
            "literary_genre": "DR",
            "price": 12.5
        }

        self.invalid_book = {
            'title': "Book new name 2",
            "author": 1,
            "isbn": 23132423534,
            "date_published": "10/02/12",
            "raiting": 4,
            "cover": "sasdsadasd",
            "prologue": 2133432423,
            "literary_genre": "XC",
            "price": 12.1232342342422423
        }

    def test_updete_valid_book(self):
        response = self.client.put(
            reverse('books:details_book', kwargs={'pk': self.book1.id}),
            data=json.dumps(self.valid_book),
            content_type='application/json'

        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_updete_invalid_book(self):
        response = self.client.put(
            reverse('books:details_book', kwargs={'pk': self.book1.id}),
            data=json.dumps(self.invalid_book),
            content_type='application/json'

        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteBookTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.author_1 = Author.objects.create(
            name='test_name_1',
            last_name="test",
            nacionalidad="MX",
            biography="xsdasdasd",
            gender="M",
            age=45,
            is_alive=True

        )
        self.book1 = Book.objects.create(
            title='Book_test_name',
            author=self.author_1,
            isbn='12345678',
            date_published=dt.datetime.now(),
            raiting=4.5,
            cover="sasdasdas",
            prologue="asdasdas",
            literary_genre="DR",
            price=12.5
        )
        self.book2 = Book.objects.create(
            title='Book_test_name 2',
            author=self.author_1,
            isbn='08765432',
            date_published=dt.datetime.now(),
            raiting=4.5,
            cover="sasdasdas",
            prologue="asdasdas",
            literary_genre="DR",
            price=13.5
        )

    def test_delete_valid_book(self):
        response = self.client.delete(
            reverse('books:details_book', kwargs={'pk': self.book1.id}),

        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_book(self):
        response = self.client.delete(
            reverse('books:details_book', kwargs={'pk': 100}),

        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
