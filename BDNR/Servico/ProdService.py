from Repository.ProdutosRepository import ProdutoRepository
from Repository.VendedorRepository import VenRepository
class ProdutoService():
    def __init__(self,prodRepo=ProdutoRepository(),venRepo=VenRepository()):
        self.RepoProd=prodRepo
        self.VenRepo=venRepo

    def acharPorNome(self,nome):
        return self.RepoProd.acharPorNome(nome)

    def criar(self,produto):
        self.RepoProd.criar(produto)

    def atualizar(self,produto):
        self.RepoProd.atualizar(produto)

    def acharTodos(self):
        print(f'===={self.pegarNomeTabela().upper()}====')
        for produto in self.RepoProd.acharTodos():
            nome=produto['prodNome']
            print(f'Id:{produto['_id']}')
            print(f'Nome:{nome}')
            print(f'Preço:{produto['prodPreco']}')
            vendedor=self.VenRepo.pegarPorId(produto['venId'])
            print(f'Vendedor:{vendedor['venNome']}')
            print()


    def deletar(self,produto):
        self.RepoProd.deletar(produto)

    def pegarNomeTabela(self):
           return self.RepoProd.pegarNomeTabela()