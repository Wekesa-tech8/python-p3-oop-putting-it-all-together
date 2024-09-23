# lib/book.py

class Book:
    def __init__(self, title, page_count, genre="Unknown", pages=None):
        self.title = title
        self.genre = genre
        self.pages = pages if pages is not None else page_count
        self.page_count = page_count  # Call the setter method

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

# Add any additional methods you need here
