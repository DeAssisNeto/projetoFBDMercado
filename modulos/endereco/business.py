from modulos.cliente.business import BusinessCliente
from modulos.endereco.dao import DaoEndereco
from modulos.endereco.endereco import Endereco
from utils import BaseValidate


class BusinessEndereco(BaseValidate):
    def __init__(self):
        self.endereco_dao = DaoEndereco()

    def _validate_rua(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        return None

    def _validate_bairro(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        return None

    def _validate_cep(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        if len(value) != Endereco.MAX_LENGTH_CEP:
            return f'O campo cep deve ter {Endereco.MAX_LENGTH_CEP} caracteres, ele contém {len(value)}'
        return None

    def _validate_id_cliente(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        cliente = BusinessCliente().get_by_id(value)
        if not cliente:
            return 'O id digitado não está associado a nenhum cliente'

    def get_all(self, filtro_nome):
        return self.endereco_dao.get_all(filtro_nome)

    def get_by_id(self, id):
        return self.endereco_dao.get_by_id(id)

    def save(self, data):
        endereco = Endereco(**data)
        endereco = self.endereco_dao.save(endereco)
        return endereco

    def delete(self, id):
        self.endereco_dao.delete(id)

    def update(self, id, data):
        self.endereco_dao.update(id, Endereco(**data))
