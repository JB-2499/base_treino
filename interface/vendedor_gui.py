from service.vendedor_service import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):

        while True:
            print("\n===== SISTEMA DE VENDEDORES =====")
            print("1 - Cadastrar vendedor")
            print("2 - Listar vendedores")
            print("3 - Consultar vendedor")
            print("4 - Atualizar vendedor")
            print("5 - Excluir vendedor")
            print("6 - Desativar vendedor")
            print("7 - Reativar vendedor")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            try:
                if opcao == "1":
                    nome = input("Nome: ")
                    observacao = input("Observação: ")

                    id_vendedor = self.services.create(
                        nome, observacao
                    )

                    print(f"Vendedor cadastrado! ID: {id_vendedor}")

                elif opcao == "2":
                    vendedores = self.services.list()

                    if not vendedores:
                        print("Nenhum vendedor cadastrado.")
                    else:
                        for vendedor in vendedores:
                            print(
                                f"ID: {vendedor.id} | "
                                f"Nome: {vendedor.name} | "
                                f"Observação: {vendedor.observation} | "
                                f"Ativo: {vendedor.active}"
                            )

                elif opcao == "3":
                    id_vendedor = int(input("Informe o ID: "))
                    vendedor = self.services.get(id_vendedor)

                    if vendedor is None:
                        print("Vendedor não encontrado.")
                    else:
                        print(f"ID: {vendedor.id}")
                        print(f"Nome: {vendedor.name}")
                        print(f"Observação: {vendedor.observation}")
                        print(f"Ativo: {vendedor.active}")

                elif opcao == "4":
                    id_vendedor = int(input("Informe o ID: "))
                    nome = input("Novo nome: ")
                    observacao = input("Nova observação: ")

                    self.services.update(
                        id_vendedor, nome, observacao
                    )

                    print("Vendedor atualizado!")

                elif opcao == "5":
                    id_vendedor = int(input("Informe o ID: "))

                    vendedor = self.services.get(id_vendedor)

                    if vendedor is None:
                        print("Vendedor não encontrado.")
                    else:
                        confirmacao = input(
                            "Deseja realmente excluir? (s/n): "
                        )

                        if confirmacao.lower() == "s":
                            self.services.delete(id_vendedor)
                            print("Vendedor excluído!")
                        else:
                            print("Operação cancelada.")

                elif opcao == "6":
                    id_vendedor = int(input("Informe o ID: "))
                    self.services.deactivate(id_vendedor)
                    print("Vendedor desativado!")

                elif opcao == "7":
                    id_vendedor = int(input("Informe o ID: "))
                    self.services.activate(id_vendedor)
                    print("Vendedor reativado!")

                elif opcao == "0":
                    print("Encerrando sistema...")
                    break

                else:
                    print("Opção inválida!")

            except ValueError as erro:
                print(f"Erro: {erro}")
