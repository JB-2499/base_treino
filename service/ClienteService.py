from entities.Cliente import Cliente
from repository.ClienteRepository import ClienteRepository

class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()
        
    def cadastrar(self, nome, cpf=None, email=None):
        if nome is None or nome.strip() == "":
            raise ValueError("O nome é obrigatório e não pode conter apenas espaços.")

        cliente = Cliente(
            nome=nome.strip(),
            cpf=cpf.strip() if cpf and cpf.strip() else None,
            email=email.strip() if email and email.strip() else None,
            ativo=True,
        )
        
        return self.repository.create(cliente)
    
    def listar(self):
        return self.repository.find_all()
    
    def buscar_por_id(self, cliente_id):
        cliente = self.repository.find_by_id(cliente_id)
        if cliente is None:
            raise LookupError("Cliente não encontrado.")
        return cliente