# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"You start reading '{self.title}' by {self.author}.")

    def get_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."


# Inherited class
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size}MB)... Done!")

    # Polymorphism: overriding method
    def read(self):
        print(f"You open the eBook '{self.title}' on your tablet.")


# Testing the classes
physical_book = Book("The Alchemist", "Paulo Coelho", 197)
ebook = EBook("Python 101", "Michael Driscoll", 250, 5)

print(physical_book.get_info())
physical_book.read()

print(ebook.get_info())
ebook.download()
ebook.read()
