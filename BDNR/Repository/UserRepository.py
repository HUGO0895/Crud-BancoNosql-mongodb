from Repository.Banco import db
from Repository.Repository import Repository

class UserRepository(Repository):
    def __init__(self, tabela='usuario', database=db):
        super().__init__(tabela, database)

    def acharPorNome(self,nome):
        return self._tabela.find_one({"nome":nome})
    

