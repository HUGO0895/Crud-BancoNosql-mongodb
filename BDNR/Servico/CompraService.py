from Repository.ComprasRepository import ComprasRepository

class CompraService():
    def __init__(self,CompRepo=ComprasRepository()):
        self.CompRepo=CompRepo

    def criar(self,compra):
        self.CompRepo.criar(compra)

    def atualizar(self,compra):
        self.CompRepo.atualizar(compra)

    def acharTodos(self):
        print(f'===={self.pegarNomeTabela().upper()}====')
        for compra in self.CompRepo.acharTodos():
            print(f'ID:{compra['_id']}')
            print(f'Produto:{compra['produto']['prodNome']}')
            print(f'Usuario:{compra['usuario']['nome']}')
            print()


    def deletar(self,compra):
        self.CompRepo.deletar(compra)


    def pegarNomeTabela(self):
       return self.CompRepo.pegarNomeTabela()

    def pegarPorId(self,id):
        return self.CompRepo.pegarPorId(id)