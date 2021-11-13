from dataclasses import dataclass


class _Book:
    def __init__(self, title=None, price=None):
        self.title, self.price = title, price


@dataclass(order=True, frozen=True)  # order : __lt__, __gt__, __le__, __ge__, frozen : __hash__
class Book:
    title: str
    price: int


print(_Book() == _Book())  # False - id 비교
print(Book('제목', 10000) == Book('제목', 10000))  # True
