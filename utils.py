

POST = 'POST'
GET = 'GET'
DELETE = 'DELETE'
PUT = 'PUT'

class BaseValidade():
    def validar(self, data, campos, objetc):
        mensagem_error = {}
        flag_error = False
        for campo in campos:
            func_name = '_validate_{}'.format(campo)
            func = hasattr(objetc, func_name)
            if func:
                func = getattr(objetc, func_name)
                data_value = func(data.get(campo, None))
                if data_value is not None:
                    mensagem_error[campo] = data_value
                    flag_error = True
        return flag_error, mensagem_error

    # def creat