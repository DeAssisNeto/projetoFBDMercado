class SQLCliente(object):
    TABLE = 'cliente'
    COLUMN_NAME = 'nome'
    SELECT_ALL = f'SELECT * FROM {TABLE}'
    SELECT_BY_ID = "SELECT * FROM {} WHERE id={}"
    SELECT_ALL_SEARCH = "SELECT * FROM {} WHERE {} ILIKE '%{}%'"
    INSERT = "INSERT INTO {} (nome, cpf) VALUES ('{}', '{}') RETURNING id"
    SELECT_BY_CPF = "SELECT * FROM {} WHERE cpf='{}'"
    DELETE = "DELETE FROM {} WHERE id={}"
