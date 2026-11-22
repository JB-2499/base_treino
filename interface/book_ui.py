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
            
            
    def _print_book(self, book):
        print("-" * 40)
        print(f"ID: {book.id}")
        print(f"Título: {book.title}")
        print(f"Sinopse: {book.synopsis or '(sem sinopse)'}")
        print(f"Situação: {book.status}")

    def list_books(self):
        books = self.services.list()

        if not books:
            print("Nenhum livro cadastrado.")
            return

        for book in books:
            self._print_book(book)
        print("-" * 40)
        
    def _read_id(self):
        value = input("Informe o ID do livro: ").strip()
        if not value.isdigit():
            print("ID inválido. Informe um número inteiro.")
            return None
        return int(value)

    def get_book(self):
        book_id = self._read_id()
        if book_id is None:
            return

        book = self.services.get(book_id)
        if book is None:
            print("Livro não encontrado.")
            return

        self._print_book(book)