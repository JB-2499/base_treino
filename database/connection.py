import os
import sqlite3

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db")

def get_connection():
    pasta = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta, "livraria.db")
    return sqlite3.connect(caminho)