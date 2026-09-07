class InterfaceCli():
    def __init__(self):
         pass
    def  escolhaDeTabelas(self):
         print("Tabelas Disponiveis:")
         print("0-Sair")
         print("1-Usuario")
         print("2-Produto")
         print("3-Vendedor")
         print("4-Compra")
         print()

    def opcoesDeAcaoDasTabelas(self,tabela):
         print(f'Opçoes da tabela {tabela}:')
         print('0-Voltar')
         print(f'1-Ver {tabela}')
         print(f'2-Criar {tabela}')
         print(f'3-Atualizar {tabela}')
         print(f'4-Deletar {tabela}')
         print()
