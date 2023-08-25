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

-- CREATE TABLE IF NOT EXISTS pedido (
--     id SERIAL PRIMARY KEY,
--     quant_produto SMALLINT,
--     id_cliente INT NOT NULL REFERENCES cliente(id),
--     status BOOLEAN
--
-- );
--
-- -- ========= INSERT PEDIDOS ================================================================================
-- INSERT INTO pedido (quant_produto, id_cliente, status) VALUES
--     (5, 1, True),
--     (3, 2, True),
--     (2, 3, True),
--     (4, 4, True),
--     (6, 5, True),
--     (7, 6, True),
--     (1, 7, True),
--     (8, 8, True),
--     (9, 9, True),
--     (10, 10, True),
--     (3, 1, True),
--     (2, 2, True),
--     (4, 3, True),
--     (6, 4, True),
--     (5, 5, True),
--     (7, 6, True),
--     (8, 7, True),
--     (9, 8, True),
--     (10, 9, True),
--     (1, 10, True),
--     (4, 1, True),
--     (6, 2, True),
--     (7, 3, True),
--     (9, 4, True),
--     (3, 5, True),
--     (5, 6, True),
--     (6, 7, True),
--     (8, 8, True),
--     (2, 9, True),
--     (7, 10, True),
--     (5, 1, True),
--     (6, 2, True),
--     (8, 3, True),
--     (9, 4, True),
--     (4, 5, True),
--     (5, 6, True),
--     (2, 7, True),
--     (3, 8, True),
--     (10, 9, True),
--     (1, 10, True);
-- -----------------------------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS pedido (
    id SERIAL PRIMARY KEY,
    quant_produto SMALLINT,
    id_produto INT NOT NULL REFERENCES produto(id),
    id_cliente INT NOT NULL REFERENCES cliente(id),
    status BOOLEAN
);

-- ========= INSERT PEDIDO ================================================================================

INSERT INTO pedido (quant_produto, id_produto, id_cliente, status)
VALUES
    (3, 5, 1, true),
    (1, 10, 2, true),
    (5, 20, 3, true),
    (2, 15, 1, true),
    (4, 25, 2, true),
    (1, 8, 3, true),
    (3, 7, 4, true),
    (2, 12, 5, true),
    (4, 27, 6, true),
    (1, 18, 7, true),
    (5, 9, 8, true),
    (3, 2, 9, true),
    (1, 28, 10, true),
    (2, 14, 1, true),
    (4, 6, 2, true),
    (5, 21, 3, true),
    (1, 17, 4, true),
    (3, 30, 5, true),
    (2, 3, 6, true),
    (4, 11, 7, true),
    (1, 23, 8, true),
    (5, 1, 9, true),
    (3, 26, 10, true),
    (2, 16, 1, true),
    (4, 19, 2, true),
    (5, 22, 3, true),
    (1, 29, 4, true),
    (3, 24, 5, true),
    (2, 13, 6, true),
    (4, 4, 7, true),
    (1, 5, 8, true),
    (5, 30, 9, true),
    (3, 12, 10, true),
    (2, 11, 1, true),
    (4, 8, 2, true),
    (5, 6, 3, true),
    (1, 25, 4, true),
    (3, 17, 5, true),
    (2, 20, 6, true),
    (4, 15, 7, true),
    (1, 2, 8, true),
    (5, 19, 9, true),
    (3, 26, 10, true),
    (2, 23, 1, true),
    (4, 9, 2, true),
    (5, 7, 3, true),
    (1, 28, 4, true),
    (3, 30, 5, true),
    (2, 1, 6, true),
    (4, 18, 7, true),
    (1, 13, 8, true),
    (5, 24, 9, true),
    (3, 22, 10, true),
    (2, 16, 1, true),
    (4, 14, 2, true),
    (5, 26, 3, true),
    (1, 10, 4, true),
    (3, 29, 5, true),
    (2, 8, 6, true),
    (4, 12, 7, true),
    (1, 27, 8, true),
    (5, 25, 9, true),
    (3, 21, 10, true),
    (2, 4, 1, true),
    (4, 3, 2, true),
    (5, 30, 3, true),
    (1, 14, 4, true),
    (3, 19, 5, true),
    (2, 11, 6, true),
    (4, 13, 7, true),
    (1, 9, 8, true),
    (5, 6, 9, true),
    (3, 16, 10, true);
-----------------------------------------------------------------------------------------------------------------

SELECT * FROM cliente p
WHERE id=21;

select * FROM cliente WHERE id=1 AND status=TRUE;
SELECT * FROM produto;
SELECT * FROM cliente;
SELECT * FROM endereco;
SELECT * FROM pedido;

SELECT count(*) FROM cliente;
