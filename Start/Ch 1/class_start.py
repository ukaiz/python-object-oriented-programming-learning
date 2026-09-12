# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    book = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None
    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        return cls.book

    # TODO: create a static method
    @staticmethod
    def get_book_list():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title):
        self.title = title


# TODO: access the class attribute
print('book types: ', Book.get_book_types())
# TODO: Create some book instances
book1 = Book("Title 1")
book2 = Book("Title 2") 

# TODO: Use the static method to access a singleton object
mergeBook = Book.get_book_list()
mergeBook.append(book1)
mergeBook.append(book2)
print(f'{mergeBook}')