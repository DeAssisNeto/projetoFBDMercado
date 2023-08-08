

POST = 'POST'
GET = 'GET'

class BaseValidade():
    def validar(self, data, campos, objetc):
        mensagem_error = {}
        flag_error = False
        for campo in campos:
            func_name = '_validate_{}'.format(campo)
            print(func_name)
            func = hasattr(objetc, func_name)
            if func:
                func = getattr(objetc, func_name)
                data_value = func(data.get(campo, None))
                if data_value is not None:
                    mensagem_error[campo] = data_value
                    flag_error = True
        return flag_error, mensagem_error