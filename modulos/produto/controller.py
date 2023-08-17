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

@app_produto.route('/<int:id>/', methods=[utils.GET])
def get_by_id(id):
    produto = business_produto.get_by_id(id)
    if produto:
        return produto.get_json()
    return make_response({"error": "Produto não encontrado"}, 404)

@app_produto.route('/<int:id>/', methods=[utils.DELETE])
def delete(id):
    prod_delet = business_produto.delete(id)
    if prod_delet:
        return make_response({"Sucess": "DELETED"}, 200)
    return make_response({"error": "Produto não encontrado"}, 404)

@app_produto.route('/<int:id>/', methods=[utils.PUT])
def update(id):
    data = request.get_json()
    error, msg = base_validate.validar(data, Produto.CAMPOS_OBRIGATORIOS, business_produto)
    if not error:
        prod_update = business_produto.update(id, data)
        if prod_update:
            return make_response({"Sucess": "UPDATED"}, 200)
        else:
            return make_response({"error": "Produto não encontrado"}, 404)
    return make_response(msg, 404)