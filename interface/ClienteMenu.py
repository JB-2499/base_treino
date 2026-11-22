from service.ClienteService import ClienteService

class ClienteMenu:
    def __init__(self):
        self.service = ClienteService()
        
    def exibir(self):
        while True:
            print("\n=== MENU CLIENTES ===")
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("3 - Consultar cliente por ID")
            print("4 - Atualizar cliente")
            print("5 - Excluir cliente")
            print("6 - Desativar cliente")
            print("0 - Voltar")
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.consultar()
            elif opcao == "4":
                self.atualizar()
            elif opcao == "5":
                self.excluir()
            elif opcao == "6":
                self.desativar()
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
            
    def consultar(self):
        print("\n--- Consultar cliente ---")
        try:
            cliente_id = int(input("Id do cliente: "))
        except ValueError:
            print("ID inválido. Digite o número")
            return
        try:
            cliente = self.service.buscar_por_id(cliente_id)
            print(cliente)
        except LookupError as erro:
            print(erro)
            
    def atualizar(self):
        print("\n--- Atualizar cliente ---")
        
        try:
            cliente_id = int(input("Id do cliente: "))
        except ValueError:
            print("ID inválido. Digite um número")
            return
        try:
            atual = self.service.buscar_por_id(cliente_id)
        except LookupError as erro:
            print(erro)
            return
        
        print(f"Dados atuais: {atual}")
        nome = input("Novo nome: ")
        cpf = input("Novo cpf (opcional): ")
        email = input("Novo email (opcional): ")
        
        try:
            cliente = self.service.atualizar(cliente_id, nome, cpf, email)
            print("Cliente atualizado com sucesso!")
            print(cliente)
        except ValueError as erro:
            print(f"Erro: {erro}")
        except LookupError as erro:
             print(erro)
             
    def excluir(self):
        print("\n--- Excluir cliente ---")

        try:
            cliente_id = int(input("ID do cliente: "))
        except ValueError:
            print("ID inválido. Digite um número.")
            return

        try:
            cliente = self.service.buscar_por_id(cliente_id)
        except LookupError as erro:
            print(erro)
            return
        
        print(f"Cliente encontrado: {cliente}")
        confirmacao = input("tem certeza que deseja excluir? (s/n): ").strip().lower()
        
        if confirmacao != "s":
            print("exclusão cancelada")
            return
        
        try:
            self.service.excluir(cliente_id)
            print("Cliente excluído com sucesso!")
        except LookupError as erro:
            print(erro)
    
    def desativar(self):
        print("\n--- Desativar cliente ---")
        
        try:
            cliente_id = int(input("Id do cliente: "))
        except ValueError:
            print("ID inválido. Digite um número")
            return
        
        try:
            cliente = self.service.desativar(cliente_id)
            print("Cliente desativado com sucesso")
            print(cliente)
        except LookupError as erro:
            print(erro)