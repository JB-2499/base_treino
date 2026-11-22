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
            
    def find_all(self):
        connection = get_connection()
        try:
            rows = connection.execute(
                "SELECT id, title, synopsis, available FROM books ORDER BY id"
            ).fetchall()
            return [self._to_book(row) for row in rows]
        finally:
            connection.close()
            
    def find_by_id(self, book_id):
        connection = get_connection()
        try:
            row = connection.execute(
                "SELECT id, title, synopsis, available FROM books WHERE id = ?",
                (book_id,),
            ).fetchone()
            return self._to_book(row) if row else None
        finally:
            connection.close()
    def update(self, book):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "UPDATE books SET title = ?, synopsis = ? WHERE id = ?",
                (book.title, book.synopsis, book.id),
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            connection.close()