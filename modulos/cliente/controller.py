from flask import Blueprint, request, make_response

import utils
from modulos.cliente.business import BusinessCliente
from modulos.cliente.cliente import Cliente

ROTA_CLIENTE = '/cliente'
app_cliente = Blueprint('app_cliente',
                        __name__,
                        url_prefix=ROTA_CLIENTE)

business_cliente = BusinessCliente()
base_validade = utils.BaseValidade()
default_error = {'message': 'Não foi possível salvar um cliente, contate o ADM'}


@app_cliente.route('/', methods=[utils.GET, utils.POST])
def get():
    if request.method == utils.POST:
        data = request.get_json()
        error, msg = base_validade.validar(data, Cliente.CAMPOS_OBRIGATORIOS, business_cliente)
        if error:
            return make_response(msg, 404)
        cliente = business_cliente.save(data)
        if cliente:
            return make_response({"id": cliente.id}, 200)
    else:
        name = request.args.get('nome', None)
        clientes = business_cliente.get_all(name)
        return clientes

@app_cliente.route('/<int:id>/', methods=[utils.GET, utils.POST])
def get_by_id(id):
    cliente = business_cliente.get_by_id(id)
    if not cliente:
        return make_response({"error": "Cliente não encontrado"}, 404)
    return cliente.get_json()
