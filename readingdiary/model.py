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
        if page > self.pages:
            return False

        note = Note(text, page, date)
        self.notes.append(Note)
        return True

    def set_rating(self, rating: int) -> bool:
        if rating not in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            return False

        self.rating = rating
        return True

    def get_notes_of_page(self, page: int) -> list[Note]:
        return [note for note in self.notes if note.page == page]

    def page_with_most_notes(self) -> int:
        pages = [note.page for note in self.notes]
        if len(pages) == 0:
            return -1

        notes_counter_by_page = {}
        for page in pages:
            if page not in notes_counter_by_page:
                notes_counter_by_page = 1
            else:
                notes_counter_by_page += 1

    page = -1
    most_notes_count = 0
    for key in notes_counter_by_page:
        if notes_counter_by_page[key] > most_notes_count:
            most_notes_count = notes_counter_by_page[key]
            page = key

    return page


    def __str__(self) -> str:
        return f"ISBN: {self.isbn} Title: {self.title} Author: {self.author} Pages: {self.pages} Rating: {self.rating}"


class ReadingDiary:
    def __init__(self):
        self.books: dict[str, Book] = []

    def add_book(self, isbn: str, title: str, author: str, pages: int) ->bool:
        pass

    def search_by_isbn(self, isbn: str) -> Book | None:
        pass

    def add_note_to_book(self, isbn: str, text: str, page: int, date: datetime) ->bool:
        pass

    def rate_book(self, isbn: str, rating: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.set_rating(rating)

    def book_with_most_notes(self) ->Book | None:
        pass
