from database.connection import get_connection
from entities.Vendedor import Vendedor

class DAOVendedor:

    def create(self, vendedor):
        connection = get_connection()

        try:
            cursor = connection.execute("""
                INSERT INTO vendedores (name, active, observation) VALUES (?, ?, ?)
            """, (vendedor.name, vendedor.active, vendedor.observation))

            connection.commit()
            return cursor.lastrowid
        
        finally:
            connection.close()

    def find_all(self):
        connection = get_connection()

        try:
            rows = connection.execute("SELECT * FROM vendedores").fetchall()

            vendedores = []
            for row in rows:
                vendedor = Vendedor (
                    name=row[1],
                    active=row[2],
                    observation=row[3],
                    id=row[0]
                )
                vendedores.append(vendedor)

            return vendedores
        
        finally:
            connection.close()

    def find_by_id(self, id):
        connection = get_connection()

        try:
            row = connection.execute("SELECT * FROM vendedores WHERE id = ?", (id,)).fetchone()

            if row is None:
                return None

            return Vendedor(
                name=row[1],
                active=row[2],
                observation=row[3],
                id=row[0]
            )
        
        finally:
            connection.close()

    def update(self, vendedor):
        connection = get_connection()

        try:
            cursor = connection.execute("""
                UPDATE vendedores SET name = ?, observation = ? WHERE id = ?
            """, (vendedor.name, vendedor.observation, vendedor.id))
            connection.commit()
            return cursor.rowcount > 0
        
        finally:
            connection.close()

    def delete(self, id):
        connection = get_connection()

        try:
            cursor =  connection.execute("DELETE FROM vendedores WHERE id = ?", (id,))

            connection.commit()
            return cursor.rowcount > 0

        finally:
            connection.close()

    def set_ativo(self, id, ativo):
        connection = get_connection()

        try:
            cursor = connection.execute("""
                UPDATE vendedores SET active = ? WHERE id = ?
            """, (ativo, id))
            connection.commit()
            return cursor.rowcount > 0
        
        finally:
            connection.close()