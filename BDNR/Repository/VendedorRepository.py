from Repository.Repository import Repository
from Repository.Banco import db
class VenRepository(Repository):
    def __init__(self,tabela='Vendedor',database=db):
        super().__init__(tabela,database)


    def acharPorNome(self,nome):
            return self._tabela.find_one({"venNome":nome})
