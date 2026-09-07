from Servico.ProdService import ProdutoService
from Servico.VenService import  VenService
class EntradaProduto():
    def __init__(self,ServProd=ProdutoService(),ServVen=VenService(),chaveProdutos=["prodNome",'prodPreco']):
        self.ServProd=ServProd
        self.ServVen=ServVen
        self.chave=chaveProdutos


    def criar(self):
        produto={}
        for chave in self.chave:
            valor=input(f'Digite um {chave}')
            valor=valor.lower() if chave=='prodNome' else valor
            produto[chave]=valor
        print(self.ServVen.acharTodos())
        venNome=input("Digite um nome de vendedor:")
        vendedor=self.ServVen.acharPorNome(venNome)
        produto['venId']=vendedor['_id']
        self.ServProd.criar(produto)

    def atualizar(self):
        prodNome=input("Digite um nome de Produto para atualizar:")
        produto=self.ServProd.acharPorNome(prodNome)
        for chave in self.chave:
           valor=input(f'Digite um {chave}')
           valor=valor.lower() if chave =='prodNome' else valor
           if valor:produto[chave]= valor 
        atualizarVen=int(input("Deseja atulizar o vendedor?(1/0)"))
        if atualizarVen:
            print(self.ServVen.acharTodos())
            venNome=input("Digite um nome de vendedor:")
            vendedor=self.ServVen.acharPorNome(venNome)
            produto['venId']=vendedor['_id']
        self.ServProd.atualizar(produto)

           
             
    def deletar(self):
        self.acharTodos()
        prodNome=input("Digite um prodNome para encontrar o produto:")
        produto=self.ServProd.acharPorNome(prodNome)
        self.ServProd.deletar(produto)

    def acharTodos(self):
             self.ServProd.acharTodos()



    def pegarNomeTabela(self):
        return self.ServProd.pegarNomeTabela()