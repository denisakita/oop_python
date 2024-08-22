class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def getBookPageCount(self):
        result = 0
        for chapter in self.chapters:
            result += chapter.page_count
        return result


class Author:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Chapter:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count


auth = Author("Auth1", "Auth")
b1 = Book("War and Peace", 39.0, auth)
b1.add_chapter(Chapter("Chap1", 12))
b1.add_chapter(Chapter("Chap2", 17))
print(auth.__str__())
print(b1.getBookPageCount())
