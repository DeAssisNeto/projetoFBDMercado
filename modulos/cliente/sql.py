class SQLCliente(object):
    TABLE = 'cliente'
    COLUMN_NOME = 'nome'
    SELECT_ALL = f'SELECT * FROM {TABLE} WHERE status=TRUE'
    SELECT_BY_ID = "SELECT * FROM {} WHERE id={} AND status=TRUE"
    SELECT_ALL_SEARCH = "SELECT * FROM {} WHERE {} ILIKE '%{}%' AND status=TRUE"
    INSERT = "INSERT INTO {} (nome, cpf, status) VALUES ('{}', '{}', TRUE) RETURNING id"
    SELECT_BY_CPF = "SELECT * FROM {} WHERE cpf='{}' AND status=TRUE"
    DELETE = "UPDATE cliente SET status=FALSE WHERE id={}"
    UPDATE = "UPDATE cliente SET nome='{}', cpf='{}' WHERE id={}"
    QUANT = F"SELECT count(*) FROM {TABLE}"
