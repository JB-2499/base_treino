from database.connection import get_connection
from entities.Cliente import Cliente

class ClienteRepository:
    def create(self, cliente):
        connection = get_connection()
        
        try:
            cursor = connection.execute(
                "INSERT INTO cliente (nome,cpf, email, ativo) values (?,?,?,?)",
                (cliente.nome, cliente.cpf, cliente.email, int(cliente.ativo))
            )
            connection.commit()
            cliente.id = cursor.lastrowid
            return cliente
        
        finally:
            connection.close()
            
    def _linha_para_cliente(self, linha):
        return Cliente(
            id_cliente=linha[0],
            nome=linha[1],
            cpf=linha[2],
            email=linha[3],
            ativo=bool(linha[4]),
        )
    
    def find_all(self):
        connection = get_connection()
        
        try:
            cursor = connection.execute(
                "SELECT id, nome, cpf, email, ativo FROM cliente ORDER BY id"
            )
            return [self._linha_para_cliente(linha) for linha in cursor.fetchall()]
        
        finally:
            connection.close()
            
    def find_by_id(self,cliente_id):
        connection = get_connection()
        
        try:
            cursor = connection.execute(
                "SELECT id, nome, cpf, email, ativo FROM cliente WHERE id = ?",
                (cliente_id,),
            )
            linha = cursor.fetchone()
            return self._linha_para_cliente(linha) if linha else None
        
        finally:
            connection.close()
            
    def update(self, cliente):
        connection = get_connection()
        
        try:
            cursor = connection.execute(
                "UPDATE cliente SET nome = ?, cpf = ?, email = ? WHERE id = ?",
                (cliente.nome, cliente.cpf, cliente.email, cliente.id),
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            connection.close()
            
            