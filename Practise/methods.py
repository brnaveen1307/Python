class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # __str__ - defines how the object should look when printed
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # __len__ - allows using len(book) to get number of pages
    def __len__(self):
        return self.pages

    # __eq__ - allows comparing two books by title
    def __eq__(self, other):
        return self.title.lower() == other.title.lower()

    # __add__ - allows adding pages of two books
    def __add__(self, other):
        return self.pages + other.pages


# Using the magic methods
book1 = Book("Atomic Habits", "James Clear", 320)
book2 = Book("Deep Work", "Cal Newport", 280)

print(book1)              # Calls __str__ → 'Atomic Habits' by James Clear
print(len(book1))         # Calls __len__ → 320
print(book1 == book2)     # Calls __eq__ → False
print(book1 + book2)      # Calls __add__ → 600
