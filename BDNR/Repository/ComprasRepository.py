from Repository.Banco import db
from Repository.Repository import Repository
class ComprasRepository(Repository):
    def __init__(self, tabela='Compras', database=db):
        super().__init__(tabela, database)

        