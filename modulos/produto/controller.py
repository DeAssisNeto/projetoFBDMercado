import traceback

from flask import Blueprint, request, make_response

import utils
from modulos.produto.business import BusinessProduto
from modulos.produto.produto import Produto

ROTA_PRODUTO = '/produto'
app_produto = Blueprint('app_produto',
                        __name__,
                        url_prefix=ROTA_PRODUTO)

business_produto = BusinessProduto()
base_validate = utils.BaseValidate()
default_error = {'message': 'Não foi possível salvar um cliente, contate o ADM'}

@app_produto.route('/', methods=[utils.GET, utils.POST])
def get():
    try:
        if request.method == utils.POST:
            data = request.get_json()
            error, msg = base_validate.validar(data, Produto.CAMPOS_OBRIGATORIOS, business_produto)
            if error:
                return make_response(msg, 404)
            produto = business_produto.save(data)
            if produto:
                return make_response({"id": produto.id}, 200)
        name = request.args.get('nome', None)
        produtos = business_produto.get_all(name)
        return produtos
    except Exception as e:
        traceback.print_exc()
        business_produto.reconnect()
    return make_response(default_error, 404)

@app_produto.route('/<int:id>/', methods=[utils.GET])
def get_by_id(id):
    try:
        produto = business_produto.get_by_id(id)
        if produto:
            return produto.get_json()
        return make_response({"error": "Produto não encontrado"}, 404)
    except Exception as e:
        traceback.print_exc()
        business_produto.reconnect()
    return make_response(default_error, 404)

@app_produto.route('/<int:id>/', methods=[utils.DELETE])
def delete(id):
    try:
        produto = business_produto.get_by_id(id)
        if produto:
            business_produto.delete(id)
            return make_response({"Sucess": "DELETED"}, 200)
        return make_response({"error": "Produto não encontrado"}, 404)
    except Exception as e:
        traceback.print_exc()
        business_produto.reconnect()
    return make_response(default_error, 404)

@app_produto.route('/<int:id>/', methods=[utils.PUT])
def update(id):
    try:
        produto = business_produto.get_by_id(id)
        if produto:
            data = request.get_json()
            error, msg = base_validate.validar(data, Produto.CAMPOS_OBRIGATORIOS, business_produto)
            if not error:
                business_produto.update(id, data)
                return make_response({"Sucess": "UPDATED"}, 200)
            return make_response(msg, 404)
        return make_response({"error": "Produto não encontrado"}, 404)
    except Exception as e:
        traceback.print_exc()
        business_produto.reconnect()
    return make_response(default_error, 404)
