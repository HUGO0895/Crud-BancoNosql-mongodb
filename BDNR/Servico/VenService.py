from Repository.VendedorRepository import VenRepository
class VenService():
    def __init__(self,VenRepo=VenRepository()):
        self.VenRepo=VenRepo

    def criar(self,vendedor):
        self.VenRepo.criar(vendedor)

    def atualizar(self,vendedor):
        self.VenRepo.atualizar(vendedor)

    def acharTodos(self):
        print(f'===={self.pegarNomeTabela().upper()}====')
        for vendedor in self.VenRepo.acharTodos():
            print(f'Nome:{vendedor['venNome']}')
            print(f'CNPJ:{vendedor['cnpj']}')
            print(f'Endereço:{vendedor['endereco']}')
            print()
            

    def deletar(self,vendedor):
        self.VenRepo.deletar(vendedor)

    def pegarNomeTabela(self):
           return self.VenRepo.pegarNomeTabela()


    def acharPorNome(self,nome):
        return self.VenRepo.acharPorNome(nome)


    def acharPorId(self,id):
        return self.VenRepo.pegarPorId(id)
