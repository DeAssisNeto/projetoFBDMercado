from modulos.cliente.dao import DaoCliente
from modulos.pedido.dao import DaoPedido
from modulos.pedido.pedido import Pedido
from modulos.produto.business import BusinessProduto
from utils import BaseValidate


class BusinessPedido(BaseValidate):
    def __init__(self):
        self.pedido_dao = DaoPedido()

    def _validate_quant_produto(self, value):
        if not value:
            return 'Este campo é obrigatório!'
        return None

    def _validate_id_produto(self, value, quant_produto=None):
        if not value:
            return 'Este campo é obrigatório!'
        quant_estoque =BusinessProduto().get_by_id(value).quantidade
        # if quant_produto and quant_estoque < quant_produto:
        #     return f'Não é possível adicionar {quant_produto} produtos pois só tem {quant_estoque} em estoque'
        return None

    def _validate_id_cliente(self, value):
        cliente = DaoCliente()
        if not value:
            return 'Este campo é obrigatório!'
        if not cliente.get_by_id(value):
            return 'O id digitado não está associado a nenhum cliente'

    def get_all(self):
        return self.pedido_dao.get_all()

    def get_by_id(self, id):
        return self.pedido_dao.get_by_id(id)

    def save(self, data):
        pedido = Pedido(**data)
        pedido = self.pedido_dao.save(pedido)
        return pedido

    def delete(self, id):
        self.pedido_dao.delete(id)

    def update(self, id, data):
        self.pedido_dao.update(id, Pedido(**data))

    def reconnect(self):
        self.pedido_dao.close_and_new_connection()