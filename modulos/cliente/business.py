from modulos.cliente.cliente import Cliente
from modulos.cliente.dao import DaoCliente
from utils import BaseValidade


class BusinessCliente(BaseValidade):
    def __init__(self):
        self.cliente_dao = DaoCliente()

    def _validate_nome(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        return None

    def _validate_cpf(self, value):
        if not value:
            return 'Este campo é obrigatório!'
#        if not str(value).isdigit():
#            return 'Este campo deve conter apenas digitos!'
        if len(value) != Cliente.MAX_LENGTH_CPF:
            return f'O campo cpf deve ter no máximo {Cliente.MAX_LENGTH_CPF} caracteres, ele contém {str(len(value))}'
        if self.cliente_dao.get_by_cpf(value):
            return 'Já existe um cliente cadastrado com esse CPF!'

    # def validar_campos(self, data, campos=list):
    #     return self.validar(data, campos)


    def get_all(self, filtro_nome):
        clientes = self.cliente_dao.get_all(filtro_nome)
        return clientes

    def get_by_id(self, id):
        return self.cliente_dao.get_by_id(id)

    def save(self, data):
        cliente = Cliente(**data)
        cliente = self.cliente_dao.save(cliente)
        return cliente
    