class SQLPedido(object):
    TABLE = 'pedido'
    SELECT_ALL = f'SELECT * FROM {TABLE} WHERE status=TRUE'
    SELECT_BY_ID = "SELECT * FROM {} WHERE id={} AND status=TRUE"
    SELECT_ALL_SEARCH = "SELECT * FROM {} WHERE {} ILIKE '%{}%' AND status=TRUE"
    INSERT = "INSERT INTO {} (quant_produto, id_produto, id_cliente, status) VALUES ({}, {}, {}, TRUE) RETURNING id"
    DELETE = "UPDATE {} SET status=FALSE WHERE id={}"
    UPDATE = "UPDATE {} SET quant_produto={}, id_produto={}, id_cliente={} WHERE id={}"
