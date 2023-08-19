from modulos.cliente.cliente import Cliente
from modulos.cliente.dao import DaoCliente
from utils import BaseValidate


class BusinessCliente(BaseValidate):
    def __init__(self):
        self.cliente_dao = DaoCliente()


    def _validate_nome(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        return None

    def _validate_cpf(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        if len(value) != Cliente.MAX_LENGTH_CPF:
            return f'O campo cpf deve ter {Cliente.MAX_LENGTH_CPF} caracteres, ele contém {len(value)}'
        if self.cliente_dao.get_by_cpf(value):
            return 'Já existe um cliente cadastrado com esse CPF!'

    def get_all(self, filtro_nome):
        clientes = self.cliente_dao.get_all(filtro_nome)
        return clientes

    def get_by_id(self, id):
        return self.cliente_dao.get_by_id(id)

    def get_by_cpf(self, cpf):
        return self.cliente_dao.get_by_cpf(cpf)

    def save(self, data):
        cliente = Cliente(**data)
        cliente = self.cliente_dao.save(cliente)
        return cliente

    def delete(self, id):
        self.cliente_dao.delete(id)

    def update(self, id, cliente_new):
        self.cliente_dao.update(id, Cliente(**cliente_new))
