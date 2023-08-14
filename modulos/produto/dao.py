from connection.ServerConnection import ConnectDataBase
from modulos.produto.produto import Produto
from modulos.produto.sql import SQLProduto


class DaoProduto(SQLProduto):
    def __init__(self):
        self.connect = ConnectDataBase()
        self.cursor = self.connect.get_cursor()

    def _execute_sql(self, sql, insert=False):
        self.cursor.execute(sql)
        if insert:
            return
        self.columns_name = [desc[0] for desc in self.cursor.description]

    def _create_objetc(self, data):
        if data:
            data = dict(zip(self.columns_name, data))
            produto = Produto(**data)
            return produto
        return None

    def get_all(self, search):
        sql = self.SELECT_ALL
        self._execute_sql(sql)
        produtos = self.cursor.fetchall()
        produtos_list = []
        for produto in produtos:
            data = dict(zip(self.columns_name, produto))
            produtos_list.append(data)
        return produtos_list

    def save(self, produto):
        sql = self.INSERT.format(self.TABLE, produto.nome, produto.preco, produto.validade, produto.quantidade)
        self.cursor.execute(sql)
        self.connect.commit()
        data = self.cursor.fetchone()
        produto.id = data[0]
        return produto
