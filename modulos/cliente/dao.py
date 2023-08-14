from connection.ServerConnection import ConnectDataBase
from modulos.cliente.cliente import Cliente
from modulos.cliente.sql import SQLCliente


class DaoCliente(SQLCliente):
    def __init__(self):
        self.connect = ConnectDataBase()
        self.cursor = self.connect.get_cursor()

    def get_all(self, search):
        sql = self.SELECT_ALL
        if search:
            sql = self.SELECT_ALL_SEARCH.format(self.TABLE, self.COLUMN_NAME, search)
        self._execute_sql(sql)
        clientes = self.cursor.fetchall()
        clientes_list = []
        for cliente in clientes:
            data = dict(zip(self.columns_name, cliente))
            clientes_list.append(data)
        return clientes_list

    def get_by_id(self, id):
        sql = self.SELECT_BY_ID.format(self.TABLE, id)
        self._execute_sql(sql)
        cliente = self._create_objetc(self.cursor.fetchone())
        return cliente

    def get_by_cpf(self, cpf):
        sql = self.SELECT_BY_CPF.format(self.TABLE, cpf)
        self._execute_sql(sql)
        cliente = self._create_objetc(self.cursor.fetchone())
        return cliente



    def _execute_sql(self, sql, insert=False):
        self.cursor.execute(sql)
        if insert:
            return
        self.columns_name = [desc[0] for desc in self.cursor.description]


    def save(self, cliente):
        sql = self.INSERT.format(self.TABLE, cliente.nome, cliente.cpf)
        #self.cursor = self.connect.get_cursor()
        self.cursor.execute(sql)
        self.connect.commit()
        data = self.cursor.fetchone()
        cliente.id = data[0]
        #self.cursor.close()
        return cliente

    def close_and_new_connection(self):
        self.connect = ConnectDataBase()
        self.cursor = self.connect.get_cursor()

    def _create_objetc(self, data):
        if data:
            data = dict(zip(self.columns_name, data))
            cliente = Cliente(**data)
            return cliente
        return None

    def delete(self, id):
        cliente = self.get_by_id(id)
        if cliente:
            sql = self.DELETE.format(self.TABLE, id)
            self.cursor.execute(sql)
            self.connect.commit()
        return cliente

    def update(self, id, cliente_new):
        cliente_old = self.get_by_id(id)
        sql = self.UPDATE_NOME.format(cliente_new.nome, id)
        sql2 = self.UPDATE_CPF.format( cliente_new.cpf, id)
        print(sql)
        if cliente_old:
            self.cursor.execute(sql)
            # self.connect.commit()
            self.cursor.execute(sql2)
            self.connect.commit()
            return True
        return False
