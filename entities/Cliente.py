class Cliente:
    def __init__(self, nome, cpf=None, email=None, ativo=True, id_cliente=None):
        self.id = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.ativo = ativo
        
        
    def __str__(self):
        situacao = "ativo" if self.ativo else "inativo"
        return f"[{self.id}] {self.nome} | cpf: {self.cpf or '-'} | email: {self.email or '-'} | {situacao}"
    
