# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    string = "this is global var"
    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.__password = "this is secret"
        # TODO: add properties

    # TODO: create instance methods
    def get_book_price(self):
        return f"{self.title} costs ${self.price}"
    def discount_book(self, discount):
        self.price = self.price - discount
        return f"{self.title} is discount by {discount} and now costs ${self.price}"
# TODO: create some book instances
b1 = Book("War and Peace", 39.95)
b2 = Book("The Catcher in the Rye", 29.95)

# TODO: print the price of book1
print(b1.get_book_price())

# TODO: try setting the discount
print(b1.discount_book(10))
# TODO: properties with double underscores are hidden by the interpreter
print(b1._Book__password)
print(f"b1 {b1.string}")
print(f"b2 {b2.string}")
