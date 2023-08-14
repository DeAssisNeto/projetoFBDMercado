from flask import Blueprint, request

import utils
from modulos.produto.business import BusinessProduto
from modulos.produto.produto import Produto

ROTA_PRODUTO = '/produto'
app_produto = Blueprint('app_produto',
                        __name__,
                        url_prefix=ROTA_PRODUTO)

business_produto = BusinessProduto()
base_validate = utils.BaseValidade()
default_error = {'message': 'Não foi possível salvar um cliente, contate o ADM'}

@app_produto.route('/', methods=[utils.GET, utils.POST])
def get():
    if request.method == utils.POST:
        data = request.get_json()
        error, msg = base_validate.validar(data, Produto.CAMPOS_OBRIGATORIOS, business_produto)

    name = request.args.get('nome', None)
    produtos = business_produto.get_all(name)
    return produtos
