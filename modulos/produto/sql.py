class SQLProduto(object):
    TABLE = 'produto'
    COLUMN_NOME = 'nome'
    SELECT_ALL = f'SELECT * FROM {TABLE} WHERE status=TRUE'
    SELECT_BY_ID = "SELECT * FROM {} WHERE id={} AND status=TRUE"
    SELECT_BY_COD_BARRAS = "SELECT * FROM {} WHERE cod_barras='{}' AND status=TRUE"
    SELECT_ALL_SEARCH = "SELECT * FROM {} WHERE {} ILIKE '%{}%' AND status=TRUE"
    INSERT = "INSERT INTO {} (nome, preco, validade, cod_barras, quantidade, status) VALUES ('{}', '{}', '{}', '{}', '{}', TRUE) RETURNING id"
    DELETE = "UPDATE produto SET status=FALSE WHERE id={}"
    UPDATE = "UPDATE produto SET nome='{}', preco='{}', validade='{}', cod_barras='{}', quantidade={}"
