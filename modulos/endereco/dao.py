from connection.ServerConnection import ConnectDataBase
from modulos.endereco.endereco import Endereco
from modulos.endereco.sql import SQLEndereco


class DaoEndereco(SQLEndereco):
    def __init__(self):
        self.connect = ConnectDataBase()
        self.cursor = self.connect.get_cursor()

    def _execute_sql(self, sql, isert=False):
        self.cursor.execute(sql)
        if isert:
            return
        self.columns_name = [desc[0] for desc in self.cursor.description]

    def _create_object(self, data):
        if data:
            data = dict(zip(self.columns_name, data))
            endereco = Endereco(**data)
            return endereco
        return None

    def get_all(self, search):
        sql = self.SELECT_ALL
        if search:
            sql = self.SELECT_ALL_SEARCH.format(search)
        self._execute_sql(sql)
        enderecos = self.cursor.fetchall()
        enderecos_list = []
        for endereco in enderecos:
            data = dict(zip(self.columns_name, endereco))
            enderecos_list.append(data)
        return enderecos_list

    def get_by_id(self, id):
        sql = self.SELECT_BY_ID.format(self.TABLE, id)
        self._execute_sql(sql)
        endereco = self._create_object(self.cursor.fetchone())
        return endereco

    def save(self, endereco):
        sql = self.INSERT.format(self.TABLE, endereco.rua, endereco.bairro, endereco.cep, endereco.id_cliente)
        self._execute_sql(sql)
        self.connect.commit()
        data = self.cursor.fetchone()
        endereco.id = data[0]
        return endereco

    def delete(self, id):
        sql = self.DELETE.format(self.TABLE, id)
        self.cursor.execute(sql)
        self.connect.commit()


    def update(self, id, endereco_new):
        sql = self.UPDATE.format(self.TABLE, endereco_new.rua, endereco_new.bairro, endereco_new.cep, endereco_new.id_cliente, id)
        self.cursor.execute(sql)
        self.connect.commit()

