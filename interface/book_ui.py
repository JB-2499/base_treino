class BookUI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        opcoes = {
            "1": ("Cadastrar livro", self.create_book),
        }

        while True:
            print("\n===== LIVROS =====")
            for chave, (nome, _) in opcoes.items():
                print(f"{chave} - {nome}")
            print("0 - Sair")

            escolha = input("Escolha uma opção: ").strip()

            if escolha == "0":
                print("Encerrando...")
                break

            if escolha in opcoes:
                opcoes[escolha][1]()
            else:
                print("Opção inválida.")

    def create_book(self):
        title = input("Título: ")
        synopsis = input("Sinopse (opcional): ")

        try:
            book = self.services.create(title, synopsis)
            print(f"Livro cadastrado com sucesso! ID: {book.id}")
        except ValueError as error:
            print(f"Erro: {error}")