class Cliente:
    NOME = 'nome'
    CPF = 'cpf'
    CAMPOS_OBRIGATORIOS = [NOME, CPF]
    MAX_LENGTH_CPF = 14

    def __init__(self, nome, cpf, status=True, id=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.status = status
        self.attributes = ["id", "nome", "cpf", "status"]

    def __str__(self):
        return f'{self.id} - {self.nome}'

    def get_json(self):
        json_data = {}
        for attr in self.attributes:
            json_data[attr] = getattr(self, attr)
        return json_data
