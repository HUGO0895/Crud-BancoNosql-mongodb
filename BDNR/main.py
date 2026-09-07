from App.App import App
from IO.entradaCompra import EntradaCompra
from IO.entradaProduto import EntradaProduto
from IO.entradaUsuario import EntradaUsuario
from IO.entradaVendedor import EntradaVendedor
from InterfaceCli.InterfaceCli import InterfaceCli
arraysEntrada=[EntradaUsuario(),EntradaProduto(),EntradaVendedor(),EntradaCompra()]
interface=InterfaceCli()
while True:
    interface.escolhaDeTabelas()
    escolhaDeRepositorio=int(input("Escolha:"))
    
    if not escolhaDeRepositorio:break

    Requisitado=arraysEntrada[escolhaDeRepositorio-1]
    while escolhaDeRepositorio:
        interface.opcoesDeAcaoDasTabelas(Requisitado.pegarNomeTabela())
        app=App(Requisitado)
        escolhaAcao=int(input("Escolha:"))
        match escolhaAcao:
            case 1:
                app.acharTodos()
            case 2:
                app.criar()
            case 3:
                app.atualizar()
            case 4:
                app.deletar()
            case 0:
                break
       


