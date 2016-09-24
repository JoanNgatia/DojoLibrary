from django.test import TestCase

# Create your tests here.
from models import Book, Category


class LibraryModelsTest(TestCase):
    """Test for correct models instantiation and creation."""

    def setUp(self):
        """Initial data for test db."""
        self.category1 = Category.objects.create(name="Fiction")
        self.category2 = Category.objects.create(name="Classics")
        self.book1 = Book.objects.create(author="Khaleid Hossein",
                                         title="Kite Runner",
                                         description="",
                                         quantity=1,
                                         category=self.category1)
        self.book2 = Book.objects.create(author="Grace Ogot",
                                         title="Promised Land",
                                         description="",
                                         quantity=1,
                                         category=self.category1)
        self.book3 = Book.objects.create(author="Charles Dickens",
                                         title="Tale of two cities",
                                         description="",
                                         quantity=1,
                                         category=self.category2)

    def test_book_model(self):
        """Test Book model instantiation and count."""
        new_book = Book.objects.create(author="Charles Dickens",
                                       title="Oliver Twist",
                                       description="",
                                       quantity=1,
                                       category=self.category2)
        self.assertIsInstance(new_book, Book)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(len(Book.objects.filter(category=self.category2)), 2)

    def test_category_model(self):
        """Test Category model instantiation and count."""
        new_category = Category.objects.create(name="Geography")
        self.assertEqual(Category.objects.count(), 3)
        self.assertIsInstance(new_category, Category)
