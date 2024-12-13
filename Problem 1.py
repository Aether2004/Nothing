class Book:
    def __init__(self, title, author, year, isbn, pages):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nISBN: {self.isbn}\nPages: {self.pages}"

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = int(input("Enter year of publication: "))
    isbn = input("Enter book ISBN: ")
    pages = int(input("Enter number of pages: "))
    book = Book(title, author, year, isbn, pages)
    books.append(book)
    print("Book added successfully!")

def display_books(books):
    if not books:
        print("No books in the library.")
        return
    for i, book in enumerate(books):
        print(f"Book {i+1}:\n{book}")

def search_book_by_title(books):
    title = input("Enter book title to search: ")
    found = False
    for book in books:
        if book() == title:
            print(f"Book Found:\n{book}")
            found = True
            break
    if not found:
        print("Book not found.")

def main():
    books = []
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book by Title")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            display_books(books)
        elif choice == '3':
            search_book_by_title(books)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
