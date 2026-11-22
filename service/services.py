from repository.dao_vendedor import DAOVendedor

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, title, description):
        # Validar dados (MUITO IMPORTANTE!!!!!)
        # Criar entidade
        # Solicitar persistência
        pass

    def list(self):
        pass

    def get(self, task_id):
        pass

    def update(self, task_id, title, description):
        pass

    def delete(self, task_id):
        pass