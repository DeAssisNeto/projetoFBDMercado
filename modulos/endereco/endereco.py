class Endereco:
    RUA = 'rua'
    BAIRRO = 'bairro'
    CEP = 'cep'
    ID_CLIENTE = 'id_cliente'
    CAMPOS_OBRIGATORIOS = [RUA, BAIRRO, CEP, ID_CLIENTE]
    MAX_LENGTH_CEP = 9

    def __init__(self, rua, bairro, cep, id_cliente, status=True, id=None):
        self.id = id
        self.rua = rua
        self.bairro = bairro
        self.cep = cep
        self.id_cliente = id_cliente
        self.status = status
        self.attibutes = ["id", "rua", "bairro", "cep", "id_cliente", "status"]

    def __str__(self):
        return f'{self.id} - {self.rua} - {self.bairro} - {self.cep}'

    def get_json(self):
        json_data = {}
        for attr in self.attibutes:
            json_data[attr] = getattr(self, attr)
        return json_data
