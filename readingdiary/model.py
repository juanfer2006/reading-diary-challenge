from datetime import datetime


class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date

    def __str__(self) -> str:
        return f"{self.date} - page {self.page}: {self.text}"


class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        self.notes: list[Note] = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if self.pages > self.pages:
            return False
        else:
            Note(text, page, date)
            self.notes.append(Note)
            return True

    def set_rating(self, rating: int) -> bool:
        pass

    def get_notes_of_page(self, page: int) -> list[Note]:
        pass

    def page_with_most_notes(self) -> int:
        pass

    def __str__(self) -> str:
        return f"ISBN: {self.isbn} Title: {self.title} Author: {self.author} Pages: {self.pages} Rating: {self.rating}"

