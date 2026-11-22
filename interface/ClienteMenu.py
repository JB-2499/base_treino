from service.ClienteService import ClienteService

class ClienteMenu:
    def __init__(self):
        self.service = ClienteService()
        
    def exibir(self):
        while True:
            print("\n=== MENU CLIENTES ===")
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("0 - Voltar")
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.listar()
            elif opcao == "0":
                break
            else:
                print("Opção inválida")
                
    def cadastrar(self):
        print("\n--- Cadastrar cliente ---")
        nome = input("Nome: ")
        cpf = input("CPF (opcional): ")
        email = input("Email (opcional): ")
        
        try:
            cliente = self.service.cadastrar(nome, cpf, email)
            print(f"Cliente cadastrado com sucesso! ID: {cliente.id}")
        except ValueError as erro:
            print(f"Erro: {erro}")
            
    def listar(self):
        print("\n--- Clientes cadastrados ---")
        clientes = self.service.listar()
        
        if not clientes:
            print("Não há clientes cadastrados")
            return
        for cliente in clientes:
            print(cliente)
            