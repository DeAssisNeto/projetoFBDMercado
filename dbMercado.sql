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
    cod_barras VARCHAR(14)
);

-- ========= INSERT PRODUTOS ================================================================================
INSERT INTO produto (nome, quantidade, preco, validade, cod_barras) VALUES
    ('Arroz (Tipo 1)', 25, 60.00, '2024-12-31', '12345678901234'),
    ('Feijão Carioca', 30, 90.00, '2025-02-28', '23456789012345'),
    ('Macarrão Espaguete', 50, 75.00, '2025-11-30', '34567890123456'),
    ('Farinha de Trigo', 40, 80.00, '2025-10-31', '45678901234567'),
    ('Açúcar Cristal', 35, 70.00, '2025-03-31', '56789012345678'),
    ('Óleo de Soja', 30, 120.00, '2025-09-30', '67890123456789'),
    ('Sal Refinado', 50, 40.00, '2025-08-31', '78901234567890'),
    ('Leite em Pó Integral', 50, 100.00, '2025-12-31', '89012345678901'),
    ('Café em Pó (Tradicional)', 40, 120.00, '2025-06-30', '90123456789012'),
    ('Achocolatado em Pó', 30, 70.00, '2025-05-31', '12345678901234'),
    ('Milho em Conserva', 40, 50.00, '2024-12-31', '23456789012345'),
    ('Ervilha em Conserva', 35, 60.00, '2025-02-28', '34567890123456'),
    ('Sardinha em Lata', 50, 75.00, '2024-11-30', '45678901234567'),
    ('Atum em Lata', 40, 90.00, '2024-10-31', '56789012345678'),
    ('Molho de Tomate', 50, 80.00, '2025-03-31', '67890123456789'),
    ('Macarrão Instantâneo (Cup Noodles)', 60, 45.00, '2025-09-30', '78901234567890'),
    ('Biscoito de Chocolate', 40, 30.00, '2025-08-31', '89012345678901'),
    ('Bolacha de Água e Sal', 50, 25.00, '2024-12-31', '90123456789012'),
    ('Extrato de Tomate', 60, 40.00, '2025-06-30', '12345678901234'),
    ('Farofa Pronta', 35, 50.00, '2025-05-31', '23456789012345'),
    ('Polvilho Azedo', 40, 35.00, '2024-12-31', '34567890123456'),
    ('Grão de Bico', 50, 60.00, '2025-02-28', '45678901234567'),
    ('Lentilha', 30, 45.00, '2024-11-30', '56789012345678'),
    ('Amendoim Torrado e Salgado', 40, 50.00, '2025-10-31', '67890123456789'),
    ('Castanha de Caju', 35, 90.00, '2025-03-31', '78901234567890'),
    ('Amêndoas', 30, 80.00, '2025-09-30', '89012345678901'),
    ('Mel Puro', 25, 120.00, '2025-08-31', '90123456789012'),
    ('Geleia de Morango', 35, 70.00, '2025-12-31', '12345678901234'),
    ('Cereal Matinal', 40, 75.00, '2025-06-30', '23456789012345'),
    ('Vinagre de Maçã', 30, 40.00, '2025-05-31', '34567890123456');

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS cliente (
    id SERIAL PRIMARY KEY,
    cpf VARCHAR(14),
    nome VARCHAR(255)
);
-- ========= INSERT CLIENTE ================================================================================
INSERT INTO cliente (cpf, nome) VALUES
    ('111.111.111-11', 'João da Silva'),
    ('222.222.222-22', 'Maria Santos'),
    ('333.333.333-33', 'Pedro Oliveira'),
    ('444.444.444-44', 'Ana Pereira'),
    ('555.555.555-55', 'José Almeida'),
    ('666.666.666-66', 'Carla Souza'),
    ('777.777.777-77', 'Rafael Lima'),
    ('888.888.888-88', 'Camila Silva'),
    ('999.999.999-99', 'Fernando Castro'),
    ('000.000.000-00', 'Mariana Rocha');

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS endereco(
    id SERIAL PRIMARY KEY,
    rua VARCHAR(255),
    bairro VARCHAR(255),
    cep VARCHAR(9),
    id_cliente INT NOT NULL REFERENCES cliente(id)
);

-- ========= INSERT ENDEREÇO ================================================================================
INSERT INTO endereco (rua, bairro, cep, id_cliente) VALUES
    ('Rua A', 'Bairro 1', '11111-111', 1),
    ('Rua B', 'Bairro 2', '22222-222', 2),
    ('Rua C', 'Bairro 3', '33333-333', 3),
    ('Rua D', 'Bairro 4', '44444-444', 4),
    ('Rua E', 'Bairro 5', '55555-555', 5),
    ('Rua F', 'Bairro 6', '66666-666', 6),
    ('Rua G', 'Bairro 7', '77777-777', 7),
    ('Rua H', 'Bairro 8', '88888-888', 8),
    ('Rua I', 'Bairro 9', '99999-999', 9),
    ('Rua J', 'Bairro 10', '00000-000', 10),
    ('Rua K', 'Bairro 1', '12345-678', 5),
    ('Rua L', 'Bairro 2', '23456-789', 6),
    ('Rua M', 'Bairro 3', '34567-890', 7),
    ('Rua N', 'Bairro 4', '45678-901', 8),
    ('Rua O', 'Bairro 5', '56789-012', 9),
    ('Rua P', 'Bairro 6', '67890-123', 10),
    ('Rua Q', 'Bairro 7', '78901-234', 1),
    ('Rua R', 'Bairro 8', '89012-345', 2),
    ('Rua S', 'Bairro 9', '90123-456', 3),
    ('Rua T', 'Bairro 10', '01234-567', 4);

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS pedido (
    id SERIAL PRIMARY KEY,
    quant_produto SMALLINT,
    id_cliente INT NOT NULL REFERENCES cliente(id)

);

-- ========= INSERT PEDIDOS ================================================================================
INSERT INTO pedido (quant_produto, id_cliente) VALUES
    (5, 1),
    (3, 2),
    (2, 3),
    (4, 4),
    (6, 5),
    (7, 6),
    (1, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (3, 1),
    (2, 2),
    (4, 3),
    (6, 4),
    (5, 5),
    (7, 6),
    (8, 7),
    (9, 8),
    (10, 9),
    (1, 10),
    (4, 1),
    (6, 2),
    (7, 3),
    (9, 4),
    (3, 5),
    (5, 6),
    (6, 7),
    (8, 8),
    (2, 9),
    (7, 10),
    (5, 1),
    (6, 2),
    (8, 3),
    (9, 4),
    (4, 5),
    (5, 6),
    (2, 7),
    (3, 8),
    (10, 9),
    (1, 10);
-----------------------------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS produto_pedido (
    id SERIAL PRIMARY KEY,
    id_produto INT NOT NULL REFERENCES produto(id),
    id_pedido INT NOT NULL REFERENCES pedido(id)
);

-- ========= INSERT PRODUTOS ================================================================================

INSERT INTO produto_pedido (id_produto, id_pedido) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15),
    (16, 16),
    (17, 17),
    (18, 18),
    (19, 19),
    (20, 20),
    (21, 21),
    (22, 22),
    (23, 23),
    (24, 24),
    (25, 25),
    (26, 26),
    (27, 27),
    (28, 28),
    (29, 29),
    (30, 30),
    (1, 31),
    (2, 32),
    (3, 33),
    (4, 34),
    (5, 35),
    (6, 36),
    (7, 37),
    (8, 38),
    (9, 39),
    (10, 40),
    (11, 1),
    (12, 2),
    (13, 3),
    (14, 4),
    (15, 5),
    (16, 6),
    (17, 7),
    (18, 8),
    (19, 9),
    (20, 10),
    (21, 11),
    (22, 12),
    (23, 13),
    (24, 14),
    (25, 15),
    (26, 16),
    (27, 17),
    (28, 18),
    (29, 19),
    (30, 20);
-----------------------------------------------------------------------------------------------------------------

SELECT * FROM cliente p
WHERE id=21;

UPDATE cliente SET nome='José Grilo'SET cpf='1234567890' WHERE id=1;

SELECT * FROM produto;
SELECT * FROM cliente;
SELECT * FROM endereco;
SELECT * FROM pedido;
SELECT * FROM produto_pedido;
