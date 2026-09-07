from Servico.VenService import VenService

class EntradaVendedor():
    def __init__(self,ServVen=VenService(),chavesVendedor=['venNome','cnpj','endereco']):
        self.ServVen=ServVen
        self.chaves=chavesVendedor

    def criar(self):
        vendedor={}
        for  chave in self.chaves:
            vendedor[chave]=input(f'Digite um {chave}')
            vendedor[chave]=vendedor[chave].lower() if chave=='venNome' else vendedor[chave]

        self.ServVen.criar(vendedor)

    def atualizar(self):
          venNome=input("Digite um nome para encontrar o usuario:")
          vendedor=self.ServVen.acharPorNome(venNome)
          print("Ajuda:Caso não queria mudar o valor digite zero ou enter")
          for chave in self.chaves:
                valor=input(f'Digite um ${chave}')
                valor= valor.lower() if chave=="venNome" else valor
                vendedor[chave]= valor if valor else vendedor[chave]
          self.ServVen.atualizar(vendedor)

    def deletar(self):
             self.acharTodos()
             usuarioNome=input("Digite um nome para encontrar o usuario:")
             usuario=self.ServVen.acharPorNome(usuarioNome)
             self.ServVen.deletar(usuario)
    
    def acharTodos(self):
             self.ServVen.acharTodos()
             
    def pegarNomeTabela(self):
          return self.ServVen.pegarNomeTabela()