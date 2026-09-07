# Crud-BancoNosql-mongodb

Aplicação de linha de comando (CLI) em Python para praticar operações **CRUD** (Create, Read, Update, Delete) em um banco de dados **NoSQL (MongoDB)**, simulando um domínio simples de marketplace com **Usuários**, **Produtos**, **Vendedores** e **Compras**.

## Sobre o projeto

O sistema simula um cenário estilo "Mercado Livre": vendedores cadastram produtos, usuários favoritam produtos e realizam compras. Todo o CRUD dessas entidades é feito via terminal, com os dados persistidos em uma instância MongoDB (local ou Atlas).

Entidades disponíveis:

- **Usuário** — nome, CPF, endereço, e-mail e lista de produtos favoritos
- **Produto** — nome, preço e vendedor associado
- **Vendedor** — nome, CNPJ e endereço
- **Compra** — associação entre um usuário e um produto

## Arquitetura

O projeto segue uma separação em camadas:

```
BDNR/
├── main.py                  # Ponto de entrada / loop principal do CLI
├── InterfaceCli/             # Exibe os menus e opções no terminal
├── IO/                        # Captura input do usuário e orquestra as chamadas (entradaUsuario, entradaProduto, entradaVendedor, entradaCompra)
├── Servico/                   # Regras de negócio (UserService, ProdService, VenService, CompraService)
├── Repository/                 # Acesso ao MongoDB (Repository base + repositórios especializados)
│   └── Banco.py                # Conexão com o MongoDB via PyMongo
└── App/App.py                  # Camada que direciona as ações (criar, atualizar, deletar, acharTodos)
```

Fluxo de uma ação: `main.py` → `InterfaceCli` (menu) → `IO/entrada*` (coleta dados) → `App` → `Servico` (regra de negócio) → `Repository` (persistência no MongoDB).

A classe `Repository` (em `Repository/Repository.py`) implementa as operações genéricas de CRUD reaproveitadas por todas as entidades, incluindo um contador de IDs sequenciais próprio (coleção `Contadora`) para simular auto-incremento no MongoDB.

## Tecnologias

- **Python 3.10+** (uso de `match/case` e f-strings com aspas simples aninhadas)
- **PyMongo** — driver oficial do MongoDB para Python
- **python-dotenv** — carregamento de variáveis de ambiente

## Pré-requisitos

- Python 3.10 ou superior
- Uma instância MongoDB acessível (local, Docker ou [MongoDB Atlas](https://www.mongodb.com/atlas))

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/HUGO0895/Crud-BancoNosql-mongodb.git
   cd Crud-BancoNosql-mongodb/BDNR
   ```

2. Instale as dependências:
   ```bash
   pip install pymongo python-dotenv
   ```

3. Crie um arquivo `.env` dentro da pasta `BDNR` com a string de conexão do MongoDB:
   ```env
   bdConect=mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net/
   ```

## Como executar

Dentro da pasta `BDNR`:

```bash
python main.py
```

O menu principal permite escolher a tabela (Usuário, Produto, Vendedor ou Compra) e, em seguida, a ação desejada:

```
Tabelas Disponiveis:
0-Sair
1-Usuario
2-Produto
3-Vendedor
4-Compra

Opçoes da tabela <tabela>:
0-Voltar
1-Ver <tabela>
2-Criar <tabela>
3-Atualizar <tabela>
4-Deletar <tabela>
```

O programa solicita os dados via `input()` no próprio terminal, de acordo com a entidade escolhida (ex.: nome, CPF, preço, vendedor associado etc.).

## Banco de dados

- Banco utilizado: `MercadoLivre`
- Coleções: `usuario`, `produto`, `vendedor`, `compra` e `Contadora` (controle interno de IDs sequenciais)

## Status

Projeto acadêmico com fins de estudo de modelagem e persistência em bancos NoSQL (MongoDB).
