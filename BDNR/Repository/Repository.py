from Repository.Banco import db
from abc import ABC
class Repository(ABC):
    def __init__(self,tabela,database=db):
        self._tabela=database[tabela]
        self._tabelaContadora=database["Contadora"]
        self._Nometabela=tabela


    def criar(self,doc):

        doc['_id']=self.atualizarID()
        self._tabela.insert_one(doc)

    def atualizar(self,Update):
        self._tabela.update_one({"_id":Update['_id']},{"$set":Update})

    def acharTodos(self):
        return list(self._tabela.find())

    def pegarNomeTabela(self):
        return self._Nometabela

    def deletar(self,doc):
        self._tabela.delete_one(doc)

    def atualizarID(self):
            resultado = self._tabelaContadora.find_one_and_update(
                {"_id": self._Nometabela},
                {"$inc": {"seq": 1}},
                upsert=True,          
                return_document=True   
            )
            return resultado["seq"]


    def pegarPorId(self,id):
         return self._tabela.find_one({'_id':id})