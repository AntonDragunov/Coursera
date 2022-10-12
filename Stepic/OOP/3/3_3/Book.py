import sys

class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
0
    def __str__(self):
        return f'Книга: {self.__title}; {self.__author}; {self.__pages}'




lst_in = list(map(str.strip, sys.stdin.readlines()))
book = Book(*lst_in)
print(book)

