from entities.book import Book


class BookServices:

    def __init__(self, repository):
        self.repository = repository

    @staticmethod
    def _validate_title(title):
        if title is None or not title.strip():
            raise ValueError("O título é obrigatório e não pode conter apenas espaços.")
        return title.strip()

    @staticmethod
    def _clean_synopsis(synopsis):
        if synopsis is None or not synopsis.strip():
            return None
        return synopsis.strip()

    def create(self, title, synopsis=None):
        title = self._validate_title(title)
        synopsis = self._clean_synopsis(synopsis)

        book = Book(title=title, synopsis=synopsis, available=False)
        book.id = self.repository.create(book)
        return book
    
    def list(self):
        return self.repository.find_all()
    
    def get(self, book_id):
        return self.repository.find_by_id(book_id)
    
    
    def update(self, book_id, title, synopsis=None):
        title = self._validate_title(title)
        synopsis = self._clean_synopsis(synopsis)

        book = self.repository.find_by_id(book_id)
        if book is None:
            return False

        book.title = title
        book.synopsis = synopsis
        return self.repository.update(book)