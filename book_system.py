import random 

#a list of available authors for random selection
authors = ["J.K. Rowling", "George Orwell", "J.R.R. Tolkien", "Jane Austen", "Charles Dickens", "Agatha Christie", "Mark Twain", "Leo Tolstoy"]

# Step 1 - Ask for the file name of the book database or use a default file name.
def ask_file_name(user_input):
    if not user_input:
        return "books.txt"
    return user_input

# Step 2 - Read the file and handle potential file errors.
def read_file(file_name):
    try:
        # Open and read the file contents, then return a list of books
        with open(file_name, 'r') as f:
            file_contents = [line.strip() for line in f.readlines()]  # Removing newline characters
        return file_contents
    except FileNotFoundError:
        # Handle the file not found error gracefully
        print("Error: File not found.")
        return []  # Return an empty list if the file is not found
# Step 3 - Randomly select an author from the `authors` list and return the selected author.
def select_random_author(authors):
    # Randomly select an author from the authors list
    return random.choice(authors)

# Step 4 - Search for the books by a particular author in the given list of books.
# If the author doesn't have any books in the list, return a message indicating so.
def find_books_by_author(author, books):
    # Create a list of books that match the author
    books_by_author = [
        book for book in books if book.split(" ~ ")[1] == author
    ]
    if books_by_author:
        return books_by_author
    else:
        return f"No books found for {author}."

# Step 5 - Print the final result in a readable format.
def final_output(books, author):
    # Print out the books by the selected author in a clear format
    if isinstance(books, list):  # Check if books are in list form
        print(f"\nBooks by {author}:")
        for book in books:
            title, _, genre, year = book.split(" ~ ")
            print(f"- {title} (Genre: {genre}, Year: {year})")
    else:
        # If no books found, books variable will be a message
        print(books)

if __name__ == "__main__":
    # Main program execution, prompting user for input and displaying the results based on the file content.
    while True:
        # Ask the user to provide a file name or use the default
        user_input = input("Enter the file name for the book database (leave empty for default 'books.txt'): ")
        books_file = ask_file_name(user_input)
        print(f"{books_file}: is your chosen file")

        # Read the books from the file and split them into a list
        books = read_file(books_file)
        if not books:
            print("Error: Unable to read the file or file is empty. Try again with a different file.\n")
            continue  # Retry if the file read failed

        # Randomly select an author from the authors list
        random_author = select_random_author(authors)
        print(f"\nRandomly selected author: {random_author}")

        # Find books by the selected author
        books_by_author = find_books_by_author(random_author, books)

        # Print the list of books found for the author
        final_output(books_by_author, random_author)

        # Ask the user if they want to check another author
        try_again = input("\nWould you like to check another author? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Thanks for using the Book Management System! Goodbye!")
            break  # Exit the loop if the user doesn't want to check again