from modulos.produto.dao import DaoProduto
from modulos.produto.produto import Produto
from utils import BaseValidade


class BusinessProduto(BaseValidade):
    def __init__(self):
        self.produto_dao = DaoProduto()

    def _validate_nome(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        return None

    def _validate_preco(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        if float(value) <= float(0):
            return f'O campo preço não pode conter valores menores ou iguais zero, foi inserido {value}'

    def _validate_validade(self, value):
        if not value:
            return 'Este campo é obrigatório!'

    def _validate_cod_barras(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        if len(value) != Produto.MAX_LENGTH_COD_BARRAS:
            return f'O campo cod_barras deve ter {Produto.MAX_LENGTH_COD_BARRAS}, ele contém {len(value)}'
        if self.produto_dao.get_by_cod_barras(value):
            return f'Já existe um produto cadastrado com esse código de barras!'

    def _validate_quantidade(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        if value<=0:
            return f'O campo quantidade não pode conter valores menores ou iguais zero, foi inserido {value}'

    def get_all(self, filtro_nome):
        return self.produto_dao.get_all(filtro_nome)

    def get_by_id(self, id):
        return self.produto_dao.get_by_id(id)

    def save(self, data):
        produto = Produto(**data)
        produto = self.produto_dao.save(produto)
        return produto

    def delete(self, id):
        return self.produto_dao.delete(id)

    def update(self, id, produto_new):
        return self.produto_dao.update(id, Produto(**produto_new))