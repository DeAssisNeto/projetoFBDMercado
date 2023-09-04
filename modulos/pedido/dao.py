from connection.ServerConnection import ConnectDataBase
from modulos.cliente.dao import DaoCliente
from modulos.pedido.pedido import Pedido
from modulos.pedido.sql import SQLPedido
from modulos.produto.dao import DaoProduto


class DaoPedido(SQLPedido):
    def __init__(self):
        self.connect = ConnectDataBase()
        self.cursor = self.connect.get_cursor()

    def _execute_sql(self, sql, insert=False):
        self.cursor.execute(sql)
        if insert:
            return
        self.columns_name = [desc[0] for desc in self.cursor.description]
        print(self.columns_name)

    def _create_objetc(self, data):
        if data:
            data = dict(zip(self.columns_name, data))
            pedido = Pedido(**data)
            return pedido
        return None

    def get_all(self):
        sql = self.SELECT_ALL
        self._execute_sql(sql)
        pedidos = self.cursor.fetchall()
        pedidos_list = []
        for pedido in pedidos:
            data = dict(zip(self.columns_name, pedido))
            data["data"] = {"data_cliente": self._get_cliente_by_id(data[self.columns_name[3]]).get_json(),
                            "data_produto": self._get_prduto_by_id(data[self.columns_name[2]]).get_json()}
            data.pop("id_produto")
            data.pop("id_cliente")
            pedidos_list.append(data)
        return pedidos_list

    def _get_cliente_by_id(self, id_cliente):
        dao_cliente = DaoCliente()
        return dao_cliente.get_by_id(id_cliente)

    def _get_prduto_by_id(self, id_produto):
        dao_produto = DaoProduto()
        return dao_produto.get_by_id(id_produto)



    def get_by_id(self, id):
        sql = self.SELECT_BY_ID.format(self.TABLE, id)
        self._execute_sql(sql)
        pedido = self._create_objetc(self.cursor.fetchone())
        return pedido

    def save(self, pedido):
        sql = self.INSERT.format(self.TABLE, pedido.quant_produto, pedido.id_produto, pedido.id_cliente)
        self.cursor.execute(sql)
        self.connect.commit()
        data = self.cursor.fetchone()
        pedido.id = data[0]
        return pedido

    def delete(self, id):
        sql = self.DELETE.format(self.TABLE, id)
        self.cursor.execute(sql)
        self.connect.commit()

    def update(self, id, pedido_new):
        sql = self.UPDATE.format(self.TABLE, pedido_new.quant_produto, pedido_new.id_produto, pedido_new.id_cliente, id)
        self.cursor.execute(sql)
        self.connect.commit()

    def close_and_new_connection(self):
        self.connect = ConnectDataBase()
        self.cursor = self.connect.get_cursor()
