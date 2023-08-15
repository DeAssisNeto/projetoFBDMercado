DROP TABLE IF EXISTS produto_pedido;
DROP TABLE IF EXISTS pedido;
DROP TABLE IF EXISTS endereco;
DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS produto;



CREATE TABLE IF NOT EXISTS produto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    quantidade SMALLINT,
    preco NUMERIC CHECK ( preco > 0 ),
    validade VARCHAR(255),
    cod_barras VARCHAR(14),
    status BOOLEAN
);

-- ========= INSERT PRODUTOS ================================================================================
INSERT INTO produto (nome, quantidade, preco, validade, cod_barras, status) VALUES
    ('Arroz (Tipo 1)', 25, 60.00, '2024-12-31', '12345678901234', True),
    ('Feijão Carioca', 30, 90.00, '2025-02-28', '23456789012345', True),
    ('Macarrão Espaguete', 50, 75.00, '2025-11-30', '34567890123456', True),
    ('Farinha de Trigo', 40, 80.00, '2025-10-31', '45678901234567', True),
    ('Açúcar Cristal', 35, 70.00, '2025-03-31', '56789012345678', True),
    ('Óleo de Soja', 30, 120.00, '2025-09-30', '67890123456789', True),
    ('Sal Refinado', 50, 40.00, '2025-08-31', '78901234567890', True),
    ('Leite em Pó Integral', 50, 100.00, '2025-12-31', '89012345678901', True),
    ('Café em Pó (Tradicional)', 40, 120.00, '2025-06-30', '90123456789012', True),
    ('Achocolatado em Pó', 30, 70.00, '2025-05-31', '12345678901234', True),
    ('Milho em Conserva', 40, 50.00, '2024-12-31', '23456789012345', True),
    ('Ervilha em Conserva', 35, 60.00, '2025-02-28', '34567890123456', True),
    ('Sardinha em Lata', 50, 75.00, '2024-11-30', '45678901234567', True),
    ('Atum em Lata', 40, 90.00, '2024-10-31', '56789012345678', True),
    ('Molho de Tomate', 50, 80.00, '2025-03-31', '67890123456789', True),
    ('Macarrão Instantâneo (Cup Noodles)', 60, 45.00, '2025-09-30', '78901234567890', True),
    ('Biscoito de Chocolate', 40, 30.00, '2025-08-31', '89012345678901', True),
    ('Bolacha de Água e Sal', 50, 25.00, '2024-12-31', '90123456789012', True),
    ('Extrato de Tomate', 60, 40.00, '2025-06-30', '12345678901234', True),
    ('Farofa Pronta', 35, 50.00, '2025-05-31', '23456789012345', True),
    ('Polvilho Azedo', 40, 35.00, '2024-12-31', '34567890123456', True),
    ('Grão de Bico', 50, 60.00, '2025-02-28', '45678901234567', True),
    ('Lentilha', 30, 45.00, '2024-11-30', '56789012345678', True),
    ('Amendoim Torrado e Salgado', 40, 50.00, '2025-10-31', '67890123456789', True),
    ('Castanha de Caju', 35, 90.00, '2025-03-31', '78901234567890', True),
    ('Amêndoas', 30, 80.00, '2025-09-30', '89012345678901', True),
    ('Mel Puro', 25, 120.00, '2025-08-31', '90123456789012', True),
    ('Geleia de Morango', 35, 70.00, '2025-12-31', '12345678901234', True),
    ('Cereal Matinal', 40, 75.00, '2025-06-30', '23456789012345', True),
    ('Vinagre de Maçã', 30, 40.00, '2025-05-31', '34567890123456', True);

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS cliente (
    id SERIAL PRIMARY KEY,
    cpf VARCHAR(14),
    nome VARCHAR(255),
    status BOOLEAN
);
-- ========= INSERT CLIENTE ================================================================================
INSERT INTO cliente (cpf, nome, status) VALUES
    ('111.111.111-11', 'João da Silva', True),
    ('222.222.222-22', 'Maria Santos', True),
    ('333.333.333-33', 'Pedro Oliveira', True),
    ('444.444.444-44', 'Ana Pereira', True),
    ('555.555.555-55', 'José Almeida', True),
    ('666.666.666-66', 'Carla Souza', True),
    ('777.777.777-77', 'Rafael Lima', True),
    ('888.888.888-88', 'Camila Silva', True),
    ('999.999.999-99', 'Fernando Castro', True),
    ('000.000.000-00', 'Mariana Rocha', True);

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS endereco(
    id SERIAL PRIMARY KEY,
    rua VARCHAR(255),
    bairro VARCHAR(255),
    cep VARCHAR(9),
    id_cliente INT NOT NULL REFERENCES cliente(id),
    status BOOLEAN
);

-- ========= INSERT ENDEREÇO ================================================================================
INSERT INTO endereco (rua, bairro, cep, id_cliente, status) VALUES
    ('Rua A', 'Bairro 1', '11111-111', 1, True),
    ('Rua B', 'Bairro 2', '22222-222', 2, True),
    ('Rua C', 'Bairro 3', '33333-333', 3, True),
    ('Rua D', 'Bairro 4', '44444-444', 4, True),
    ('Rua E', 'Bairro 5', '55555-555', 5, True),
    ('Rua F', 'Bairro 6', '66666-666', 6, True),
    ('Rua G', 'Bairro 7', '77777-777', 7, True),
    ('Rua H', 'Bairro 8', '88888-888', 8, True),
    ('Rua I', 'Bairro 9', '99999-999', 9, True),
    ('Rua J', 'Bairro 10', '00000-000', 10, True),
    ('Rua K', 'Bairro 1', '12345-678', 5, True),
    ('Rua L', 'Bairro 2', '23456-789', 6, True),
    ('Rua M', 'Bairro 3', '34567-890', 7, True),
    ('Rua N', 'Bairro 4', '45678-901', 8, True),
    ('Rua O', 'Bairro 5', '56789-012', 9, True),
    ('Rua P', 'Bairro 6', '67890-123', 10, True),
    ('Rua Q', 'Bairro 7', '78901-234', 1, True),
    ('Rua R', 'Bairro 8', '89012-345', 2, True),
    ('Rua S', 'Bairro 9', '90123-456', 3, True),
    ('Rua T', 'Bairro 10', '01234-567', 4, True);

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS pedido (
    id SERIAL PRIMARY KEY,
    quant_produto SMALLINT,
    id_cliente INT NOT NULL REFERENCES cliente(id),
    status BOOLEAN

);

-- ========= INSERT PEDIDOS ================================================================================
INSERT INTO pedido (quant_produto, id_cliente, status) VALUES
    (5, 1, True),
    (3, 2, True),
    (2, 3, True),
    (4, 4, True),
    (6, 5, True),
    (7, 6, True),
    (1, 7, True),
    (8, 8, True),
    (9, 9, True),
    (10, 10, True),
    (3, 1, True),
    (2, 2, True),
    (4, 3, True),
    (6, 4, True),
    (5, 5, True),
    (7, 6, True),
    (8, 7, True),
    (9, 8, True),
    (10, 9, True),
    (1, 10, True),
    (4, 1, True),
    (6, 2, True),
    (7, 3, True),
    (9, 4, True),
    (3, 5, True),
    (5, 6, True),
    (6, 7, True),
    (8, 8, True),
    (2, 9, True),
    (7, 10, True),
    (5, 1, True),
    (6, 2, True),
    (8, 3, True),
    (9, 4, True),
    (4, 5, True),
    (5, 6, True),
    (2, 7, True),
    (3, 8, True),
    (10, 9, True),
    (1, 10, True);
-----------------------------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS produto_pedido (
    id SERIAL PRIMARY KEY,
    id_produto INT NOT NULL REFERENCES produto(id),
    id_pedido INT NOT NULL REFERENCES pedido(id),
    status BOOLEAN
);

-- ========= INSERT PRODUTOS ================================================================================

INSERT INTO produto_pedido (id_produto, id_pedido, status) VALUES
    (1, 1, True),
    (2, 2, True),
    (3, 3, True),
    (4, 4, True),
    (5, 5, True),
    (6, 6, True),
    (7, 7, True),
    (8, 8, True),
    (9, 9, True),
    (10, 10, True),
    (11, 11, True),
    (12, 12, True),
    (13, 13, True),
    (14, 14, True),
    (15, 15, True),
    (16, 16, True),
    (17, 17, True),
    (18, 18, True),
    (19, 19, True),
    (20, 20, True),
    (21, 21, True),
    (22, 22, True),
    (23, 23, True),
    (24, 24, True),
    (25, 25, True),
    (26, 26, True),
    (27, 27, True),
    (28, 28, True),
    (29, 29, True),
    (30, 30, True),
    (1, 31, True),
    (2, 32, True),
    (3, 33, True),
    (4, 34, True),
    (5, 35, True),
    (6, 36, True),
    (7, 37, True),
    (8, 38, True),
    (9, 39, True),
    (10, 40, True),
    (11, 1, True),
    (12, 2, True),
    (13, 3, True),
    (14, 4, True),
    (15, 5, True),
    (16, 6, True),
    (17, 7, True),
    (18, 8, True),
    (19, 9, True),
    (20, 10, True),
    (21, 11, True),
    (22, 12, True),
    (23, 13, True),
    (24, 14, True),
    (25, 15, True),
    (26, 16, True),
    (27, 17, True),
    (28, 18, True),
    (29, 19, True),
    (30, 20, True);
-----------------------------------------------------------------------------------------------------------------

SELECT * FROM cliente p
WHERE id=21;

select * FROM cliente WHERE id=1 AND status=TRUE;
SELECT * FROM produto;
SELECT * FROM cliente;
SELECT * FROM endereco;
SELECT * FROM pedido;
SELECT * FROM produto_pedido;

SELECT count(*) FROM cliente