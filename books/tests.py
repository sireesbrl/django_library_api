from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An excellent subtitle",
            author="Tom Christie",
            isbn="1234567890123",
        )

    def test_book_content(self):
        self.assertEqual("A good title", self.book.title)
        self.assertEqual("An excellent subtitle", self.book.subtitle)
        self.assertEqual("Tom Christie", self.book.author)
        self.assertEqual("1234567890123", self.book.isbn)

    def test_book_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "excellent subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")
