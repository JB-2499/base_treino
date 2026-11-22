
from repository.dao_vendedor import DAOVendedor
from service.vendedor_service import Services

repository = DAOVendedor()
service = Services(repository)

# CREATE
print("Criando vendedor...")
id_vendedor = service.create("João", "Vendedor de teste")

print("ID criado:", id_vendedor)

# LIST
print("\nListando vendedores...")
vendedores = service.list()

for vendedor in vendedores:
    print(
        vendedor.id,
        vendedor.name,
        vendedor.active,
        vendedor.observation
    )

# GET
print("\nBuscando vendedor...")
vendedor = service.get(id_vendedor)

print(vendedor.name)

# UPDATE
print("\nAtualizando vendedor...")
service.update(id_vendedor, "João Silva", "Observação atualizada")

vendedor = service.get(id_vendedor)

print(vendedor.name)
print(vendedor.observation)

# DELETE
print("\nExcluindo vendedor...")
service.delete(id_vendedor)

print("Vendedor excluído!")

# Verificando exclusão
print("\nBuscando vendedor excluído...")
print(service.get(id_vendedor))
