import traceback

from flask import Blueprint, request, make_response

import utils
from modulos.cliente.business import BusinessCliente
from modulos.cliente.cliente import Cliente

ROTA_CLIENTE = '/cliente'
app_cliente = Blueprint('app_cliente',
                        __name__,
                        url_prefix=ROTA_CLIENTE)

business_cliente = BusinessCliente()
base_validate = utils.BaseValidate()
default_error = {'message': 'Não foi possível salvar um cliente, contate o ADM'}


@app_cliente.route('/', methods=[utils.GET, utils.POST])
def get():
    try:
        if request.method == utils.POST:
            data = request.get_json()
            error, msg = base_validate.validar(data, Cliente.CAMPOS_OBRIGATORIOS, business_cliente)
            if error:
                return make_response(msg, 404)
            cliente = business_cliente.save(data)
            if cliente:
                return make_response({"id": cliente.id}, 200)
        else:
            name = request.args.get('nome', None)
            clientes = business_cliente.get_all(name)
            return clientes
    except Exception as e:
        traceback.print_exc()
        business_cliente.reconnect()
    return make_response(default_error, 404)

@app_cliente.route('/<int:id>/', methods=[utils.GET])
def get_by_id(id):
    try:
        cliente = business_cliente.get_by_id(id)
        if cliente:
            return cliente.get_json()
        return make_response({"error": "Cliente não encontrado"}, 404)
    except Exception as e:
        traceback.print_exc()
        business_cliente.reconnect()

@app_cliente.route('/<int:id>/', methods=[utils.DELETE])
def delete(id):
    try:
        cliente = business_cliente.get_by_id(id)
        if cliente:
            business_cliente.delete(id)
            return make_response({"Sucess": "DELETED"}, 200)
        return make_response({"error": "Cliente não encontrado"}, 404)
    except Exception as e:
        traceback.print_exc()
        business_cliente.reconnect()

@app_cliente.route('/<int:id>', methods=[utils.PUT])
def update(id):
    try:
        cliente = business_cliente.get_by_id(id)
        if cliente:
            data = request.get_json()
            error, msg = base_validate.validar(data, Cliente.CAMPOS_OBRIGATORIOS, business_cliente)
            if not error:
                business_cliente.update(id, data)
                return make_response({"Sucess": "UPDATED"}, 200)
            return make_response(msg, 404)
        return make_response({"error": "Cliente não encontrado"}, 404)
    except Exception as e:
        traceback.print_exc()
        business_cliente.reconnect()
