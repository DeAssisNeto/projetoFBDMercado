from flask import Flask

from modulos.cliente.business import BusinessCliente
from modulos.cliente.controller import app_cliente
from modulos.cliente.dao import DaoCliente
from utils import GET

app = Flask(__name__)
app.register_blueprint(app_cliente)

@app.route('/', methods=[GET])
def home():
    return {}

app.run()