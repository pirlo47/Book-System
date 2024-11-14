Book System
This Book System is a command-line application that lets users select and interact with a collection of books and authors. The system loads book data from a text file, allowing users to search for books by title, author, genre, or publication year.

How It Works
The program reads book entries from books.txt where each entry is in the format Title ~ Author ~ Genre ~ Year.
Users can run the program, follow on-screen prompts to interact with the book data, and perform actions such as searching or listing books.
The system includes unittests to ensure technical correctness, including a test that verifies the creation of a specific file, myfile.txt, containing the entry George Orwell ~ 1984.

Getting Started 
1.Run the program 
To start the program, use:
python3 book_system.py

2. Running Tests 
to confirm functionality, run the unittests:
python3 -m unittest tests/test_book_system.py
