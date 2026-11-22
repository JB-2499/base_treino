from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        connection.execute("""
        CREATE TABLE IF NOT EXISTS vendedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        active INTEGER NOT NULL DEFAULT 0,
        observation TEXT NOT NULL DEFAULT '')
        """)

        total = connection.execute("SELECT COUNT(*) FROM vendedores").fetchone()[0]
        
        if total == 0:
            connection.execute(
                "INSERT INTO vendedores (name, active, observation) VALUES (?, ?, ?)",
                ("João", 1, "Vendedor experiente")
            )
        
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")