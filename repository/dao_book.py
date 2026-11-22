from database.connection import get_connection
from entities.book import Book


class DAOBook:

    @staticmethod
    def _to_book(row):
        return Book(id=row[0], title=row[1], synopsis=row[2], available=bool(row[3]))

    def create(self, book):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "INSERT INTO books (title, synopsis, available) VALUES (?, ?, ?)",
                (book.title, book.synopsis, int(book.available)),
            )
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()