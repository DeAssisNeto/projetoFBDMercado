class Produto:
    NOME = 'nome'
    PRECO = 'preco'
    VALIDADE = 'validade'
    COD_BARRAS = 'cod_barras'
    QUANTIDADE = 'quantidade'
    CAMPOS_OBRIGATORIOS = [NOME, PRECO, VALIDADE, COD_BARRAS, QUANTIDADE]
    MAX_LENGTH_COD_BARRAS = 14

    def __init__(self, nome, preco, validade, cod_barras, quantidade, status=True, id=None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.validade = validade
        self.cod_barras = cod_barras
        self.quantidade = quantidade
        self.status = status
        self.attributes = ["id", "nome", "preco", "validade", "cod_barras", "quantidade", "status"]

    def __str__(self):
        return f'{self.id} - {self.nome}'

    def get_json(self):
        json_data = {}
        for attr in self.attributes:
            json_data[attr] = getattr(self, attr)
        return json_data