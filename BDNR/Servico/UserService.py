from Repository.UserRepository import UserRepository
from Repository.VendedorRepository import VenRepository
class UserService():
    def __init__(self,userRepo=UserRepository(),venRepo=VenRepository()):
        self.RepoUser=userRepo
        self.VenRepo=venRepo

    def criar(self,Usuario):
        self.RepoUser.criar(Usuario)

    def atualizar(self,Usuario):
        self.RepoUser.atualizar(Usuario)


    def acharTodos(self):
        print(f'===={self.pegarNomeTabela().upper()}====')
        for usuario in self.RepoUser.acharTodos():
            print(f'Id:{usuario['_id']}')
            print(f'Nome:{usuario['nome']}')
            print(f'Email:{usuario['userEmail']}')
            print(f'CPF:{usuario['cpf']}')
            print(f'Endereço:{usuario['endereco']}')
            print("Favoritos:")
            for produto in usuario['favoritos']:
                print(f'Id:{produto['_id']}')
                print(f'Nome:{produto['prodNome']}')
                print(f'Preço:{produto['prodPreco']}')
                vendedor=self.VenRepo.pegarPorId(produto['venId'])
                print(f'Vendedor:{vendedor['venNome']}')
            print()

    def acharPorNome(self,nome):
       return self.RepoUser.acharPorNome(nome)        

    def deletar(self,usuario):
        self.RepoUser.deletar(usuario)

    def pegarNomeTabela(self):
           return self.RepoUser.pegarNomeTabela()