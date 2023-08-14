class SQLProduto(object):
    TABLE = 'produto'
    COLUMN_NOME = 'nome'
    SELECT_ALL = f'SELECT * FROM {TABLE}'
    SELECT_BY_ID = "SELECT * FROM {} WHERE id={}"
    SELECT_ALL_SEARCH = "SELECT * FROM {} WHERE {} ILIKE '%{}%'"
    INSERT = "INSERT INTO {} (nome, preco, validade, cod_barras, quantidade) VALUES ('{}', '{}', '{}', '{}', '{}') RETURNING id"
