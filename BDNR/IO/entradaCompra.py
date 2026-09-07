from Servico.CompraService import CompraService
from Servico.ProdService import ProdutoService
from Servico.UserService import UserService

class EntradaCompra():
    def __init__(self,ServComp=CompraService(),ServProd=ProdutoService(),ServUser=UserService()):
        self.ServComp=ServComp
        self.ServProd=ServProd
        self.ServUser=ServUser

    def criar(self):
        compra={}
        self.ServUser.acharTodos()
        userName=input("Digite um nome de usuario:").lower()
        usuario=self.ServUser.acharPorNome(userName)
        compra['usuario']=usuario
        prodNome=input("Digite um nome de usuario:").lower()
        produto=self.ServProd.acharPorNome(prodNome)
        compra['produto']=produto
        self.ServComp.criar(compra)

    def atualizar(self):
        self.ServComp.acharTodos()
        compraId=int(input("Digite um id de compra:"))
        compra=self.ServComp.pegarPorId(compraId)
        usuario=compra['usuario']
        produto=compra['Produtos']
        userName=input("Digite um nome de usuario caso queira atualizar,se nao quiser aperte enter:").lower()
        if userName:usuario=self.ServUser.acharPorNome(userName)
        prodNome=input("Digite um nome de usuario caso queira atualizar,se nao quiser aperte enter:").lower()
        if prodNome:produto=self.ServUser.acharPorNome(prodNome)
        compra['Produtos']=produto
        compra['usuario']=usuario
        self.ServComp.atualizar(compra)

    def deletar(self):
        self.acharTodos()
        prodNome=int(input("Digite um Id de compras para encontrar o produto:"))
        produto=self.ServComp.pegarPorId(prodNome)
        self.ServComp.deletar(produto)
        
    def acharTodos(self):
        self.ServComp.acharTodos()


    def pegarNomeTabela(self):
        return self.ServComp.pegarNomeTabela()