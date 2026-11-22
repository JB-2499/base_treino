from install import install
from interface.vendedor_gui import UI
from service.vendedor_service import Services
from repository.dao_vendedor import DAOVendedor


def main():
    install()

    repository = DAOVendedor()
    services = Services(repository)

    ui = UI(services)
    ui.show_principal_menu()


if __name__ == "__main__":
    main()
    