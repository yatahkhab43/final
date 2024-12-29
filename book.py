class BookStack:
    def __init__(self):
        self.stack = []

    def borrow(self, book):
        self.stack.append(book)

    def return_book(self):
        return self.stack.pop() if self.stack else "No books borrowed"

books = BookStack()
books.borrow("Book A")
books.borrow("Book B")
print("Returned:", books.return_book())
