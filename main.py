from flask import Flask

from modulos.cliente.controller import app_cliente
from modulos.endereco.controller import app_endereco
from modulos.pedido.controller import app_pedido
from modulos.produto.controller import app_produto
from utils import GET

app = Flask(__name__)
app.register_blueprint(app_cliente)
app.register_blueprint(app_produto)
app.register_blueprint(app_endereco)
app.register_blueprint(app_pedido)

@app.route('/', methods=[GET])
def home():
    return {}

app.run()

"""
Rever a parte que retorna o pedido com o id do produto e do cliente. Retornar todas as informações "usáveis", não apenas o id. (DONE)
Rever a estrutura das tabelas
Acrescentar tabelas para complementar o projeto (tabela para vendas, tabela(s) para gerenciamento de estoque)
Fazer a mascara para cpf, codigo de barrra, cep, etc.
Fazer uma consulta de pedidos por clientes.
"""
