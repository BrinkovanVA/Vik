def decorator(method_to_decorate):
    def wrapper(self, other):
        # (1, 2) + (3, -1) = (2, 1)
        res = method_to_decorate(self, other)
        print(f"{self} + {other} = {res}")
        return res
    return wrapper

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    @decorator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

a = Vector(1, 2)
b = Vector(3, 5)
print(a + b)