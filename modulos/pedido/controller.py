from flask import Blueprint, request, make_response

import utils
from modulos.pedido.business import BusinessPedido
from modulos.pedido.pedido import Pedido

ROTA_PEDIDO = '/pedido'
app_pedido = Blueprint('app_pedido',
                       __name__,
                       url_prefix=ROTA_PEDIDO)

business_pedido = BusinessPedido()
base_validate = utils.BaseValidate()
default_error = {'message': 'Não foi possível salvar um pedido, contate o ADM'}

@app_pedido.route('/', methods=[utils.GET, utils.POST])
def get():
    if request.method == utils.POST:
        data = request.get_json()
        error, msg = base_validate.validar(data, Pedido.CAMPOS_OBRIGATORIOS, business_pedido)
        if error:
            return make_response(msg, 404)
        pedido = business_pedido.save(data)
        if pedido:
            return make_response({"id": pedido.id}, 200)
    pedidos = business_pedido.get_all()
    return pedidos

@app_pedido.route('/<int:id>/', methods=[utils.GET])
def get_by_id(id):
    pedido = business_pedido.get_by_id(id)
    if pedido:
        return pedido.get_json()
    return make_response({"error": "Pedido não encontrado"}, 404)

@app_pedido.route('/<int:id>', methods=[utils.DELETE])
def delete(id):
    pedido = business_pedido.get_by_id(id)
    if pedido:
        business_pedido.delete(id)
        return make_response({"Sucess": "DELETED"}, 200)
    return make_response({"error": "Pedido não encontrado"}, 404)

@app_pedido.route('/<int:id>', methods=[utils.PUT])
def update(id):
    pedido = business_pedido.get_by_id(id)
    if pedido:
        data = request.get_json()
        error, msg = base_validate.validar(data, Pedido.CAMPOS_OBRIGATORIOS, business_pedido)
        if not error:
            business_pedido.update(id, data)
            return make_response({"Sucess": "UPDATED"}, 200)
        return make_response(msg, 404)
    return make_response({"error": "Pedido não encontrado"}, 404)
