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