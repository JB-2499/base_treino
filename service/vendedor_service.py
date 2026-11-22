from entities.Vendedor import Vendedor
from repository.dao_vendedor import DAOVendedor

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, name, observation):
        if name is None or name.strip() == "":
            raise ValueError("Nome não pode estar vazio.")

        vendedor = Vendedor(name=name, active=True, observation=observation)
        return self.repository.create(vendedor)

    def list(self):
        return self.repository.find_all()

    def get(self, id):
        return self.repository.find_by_id(id)

    def update(self, id, name, observation):
        if name is None or name.strip() == "":
            raise ValueError("Nome não pode estar vazio.")

        vendedor = self.repository.find_by_id(id)
        if vendedor is None:
            raise ValueError("Vendedor não encontrado.")

        vendedor.name = name
        vendedor.observation = observation
        self.repository.update(vendedor)

    def delete(self, id):
        vendedor = self.repository.find_by_id(id)

        if vendedor is None:
            raise ValueError("Vendedor não encontrado.")
        
        self.repository.delete(id)

    def deactivate(self, id):
        vendedor = self.repository.find_by_id(id)

        if vendedor is None:
            raise ValueError("Vendedor não encontrado.")

        vendedor.active = False
        self.repository.update(vendedor)

    def activate(self, id):
        vendedor = self.repository.find_by_id(id)

        if vendedor is None:
            raise ValueError("Vendedor não encontrado.")

        vendedor.active = True
        self.repository.update(vendedor)