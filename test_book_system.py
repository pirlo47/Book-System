import unittest 
from unittest.mock import patch, mock_open 
from io import StringIO
import book_system 

class BookSysytemTestCase(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data = "J.k. Rowling ~ Harry Potter ~ Fiction ~ 1997\nGeorge Orwell ~ 1984 ~ Dystopian ~ 1949"))
    def test_read_file_success(self):
        #test that the read_file function correctly reads the file contents
        books = book_system.read_file("books.txt")
        expected_books =  [
            "J.K. Rowling ~ Harry Potter ~ Fiction ~ 1997",
            "George Orwell ~ 1984 ~ Dystopian ~ 1949"
        ]
        self.assertEqual(books, expected_books)

    if __name__ == '__main__':
        unittest.main()