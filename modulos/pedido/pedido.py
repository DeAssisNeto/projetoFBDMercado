class Pedido:
    QUANT_PRODUTO = 'quant_produto'
    ID_PRODUTO = 'id_produto'
    ID_CLIENTE = 'id_cliente'
    CAMPOS_OBRIGATORIOS = [QUANT_PRODUTO, ID_PRODUTO, ID_CLIENTE]




    def __init__(self, quant_produto, id_produto, id_cliente, status=True, id=None):
        self.id = id
        self.quant_produto = quant_produto
        self.id_produto = id_produto
        self.id_cliente = id_cliente
        self.status = status
        self.attributes = ["id", "quant_produto", "id_produto", "id_cliente", "status"]

    def __str__(self):
        return f'{self.id}, {self.quant_produto}'

    def get_json(self):
        json_data = {}
        for attr in self.attributes:
            json_data[attr] = getattr(self, attr)
        return json_data

"""
{
    "id": "",
    "data": {
        "cliente": {
            
        },
        "produto": {
            
        }
    },
    "status": "boolean"
}
"""
