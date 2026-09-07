from Servico.UserService import UserService
from Servico.ProdService import ProdutoService
from Servico.CompraService import CompraService
class EntradaUsuario():
    def __init__(self,ServUsuario=UserService(),ServProduto=ProdutoService(),ServComp=CompraService(),chavesUsuario=["nome","cpf","endereco","userEmail"]):
        self.ServUser=ServUsuario
        self.ServProd=ServProduto
        self.ServComp=ServComp
        self.chaves=chavesUsuario
    def criar(self):
            usuario={}
            for  chave in self.chaves:
               usuario[chave]=input(f'Digite um {chave}')
               usuario[chave]=usuario[chave].lower() if chave=='nome' else usuario[chave]
            
            usuario['favoritos']=[]
            print("Ajuda:Digite 0 se não quiser")
            quantosFavs=int(input("Desenja adiconar quantos produtos como favoritos para esse usuario:"))
            print(self.ServProd.acharTodos())
            for x in range(quantosFavs):
                 nomeProduto=input("Digite um nome valido de produto:")
                 produto=self.ServProd.acharPorNome(nomeProduto)
                 usuario['favoritos'].append(produto) if produto else print("Produto não foi encontrado")

            print(usuario)
            self.ServUser.criar(usuario)

    def atualizar(self):
         usuarioNome=input("Digite um nome para encontrar o usuario:")
         usuario=self.ServUser.acharPorNome(usuarioNome)
         print(usuario)
         print("Ajuda:Caso não queria mudar o valor digite zero ou enter")
         for chave in self.chaves:
              valor=input(f'Digite um ${chave}').lower()
              valor= valor.lower() if chave=="nome" else valor

              if valor:usuario[chave]= valor 

         opcao=int(input("Digite 1 para adicionar favoritos 2 para deletar e 0 para pular essa etapa"))
         match opcao:
              case 1:
                    quantosFavs=int(input("Desenja adiconar quantos produtos como favoritos para esse usuario:"))
                    print(self.ServProd.acharTodos())
                    for x in range(quantosFavs):
                         nomeProduto=input("Digite um nome valido de produto:")
                         produto=self.ServProd.acharPorNome(nomeProduto)
                         usuario['favoritos'].append(produto) if produto else print("Produto não foi encontrado")
              case 2:
                   for produto in usuario['favoritos']:
                        deletar=int(input("1 para deletar e 0 ou enter para passar"))
                        if deletar:self.ServProd.deletar(produto)
          
         self.ServUser.atualizar(usuario)
               
              
     
          
         
    def deletar(self):
         self.acharTodos()
         usuarioNome=input("Digite um nome para encontrar o usuario:")
         usuario=self.ServUser.acharPorNome(usuarioNome)
         self.ServUser.deletar(usuario)

    def acharTodos(self):
         self.ServUser.acharTodos()


    def pegarNomeTabela(self):
         return self.ServUser.pegarNomeTabela()