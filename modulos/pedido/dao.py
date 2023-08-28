from connection.ServerConnection import ConnectDataBase
from modulos.pedido.pedido import Pedido
from modulos.pedido.sql import SQLPedido


class DaoPedido(SQLPedido):
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
            pedidos_list.append(data)
        return pedidos_list

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
