from flask import Blueprint, request, make_response

import utils
from modulos.endereco.business import BusinessEndereco
from modulos.endereco.endereco import Endereco

ROTA_ENDERECO = '/endereco'
app_endereco = Blueprint('app_endereco',
                         __name__,
                         url_prefix=ROTA_ENDERECO)
business_endereco = BusinessEndereco()
base_validate = utils.BaseValidate()
default_error = {'message': 'Não foi possível salvar um endereco, contate o ADM'}

@app_endereco.route('/', methods=[utils.GET, utils.POST])
def get():
    if request.method == utils.POST:
        data = request.get_json()
        error, msg = base_validate.validar(data, Endereco.CAMPOS_OBRIGATORIOS, business_endereco)
        if error:
            return make_response(msg, 404)
        endereco = business_endereco.save(data)
        if endereco:
            return make_response({"id": endereco.id}, 200)
    name = request.args.get('nome', None)
    return business_endereco.get_all(name)

@app_endereco.route('/<int:id>/', methods=[utils.GET])
def get_by_id(id):
    endereco = business_endereco.get_by_id(id)
    if endereco:
        return endereco.get_json()
    return make_response({"error": "Endereço não encontrado"}, 404)

@app_endereco.route('/<int:id>/', methods=[utils.DELETE])
def delete(id):
    endereco = business_endereco.get_by_id(id)
    if endereco:
        business_endereco.delete(id)
        return make_response({"Sucess": "DELETED"}, 200)
    return make_response({"error": "Endereço não encontrado"}, 404)

@app_endereco.route('/<int:id>/', methods=[utils.PUT])
def update(id):
    endereco = business_endereco.get_by_id(id)
    if endereco:
        data = request.get_json()
        error, msg = base_validate.validar(data, Endereco.CAMPOS_OBRIGATORIOS, business_endereco)
        if not error:
            business_endereco.update(id, data)
            return make_response({"Sucess": "UPDATED"}, 200)
        return make_response(msg, 404)
    return make_response({"error": "Endereco não encontrado"}, 404)
