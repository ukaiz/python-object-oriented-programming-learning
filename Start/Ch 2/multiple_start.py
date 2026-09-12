# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        self.prop1 = "prop1"


class B(A):
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"


class C(B):
    def __init__(self):
        super().__init__()
    def str(self):
        return f"{self.prop1} {self.prop2}"

c = C()
b = B()
print(c.prop1)