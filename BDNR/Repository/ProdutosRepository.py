from Repository.Banco import db
from Repository.Repository import Repository 

class ProdutoRepository(Repository):
    def __init__(self, tabela='Produtos', database=db):
        super().__init__(tabela, database)

    def acharPorNome(self,nome):
        return self._tabela.find_one({"prodNome":nome})