CREATE DATABASE crypto_db;

USE crypto_db;


-- =========================================
-- TABELA: BLOCKCHAIN
-- =========================================
CREATE TABLE blockchain (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    simbolo VARCHAR(20) NOT NULL,
    algoritmo_consenso VARCHAR(50),
    rede_principal VARCHAR(50),
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uk_blockchain_nome
        UNIQUE (nome),

    CONSTRAINT uk_blockchain_simbolo
        UNIQUE (simbolo)
);


-- =========================================
-- TABELA: CRIPTOMOEDA
-- =========================================
CREATE TABLE criptomoeda (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    blockchain_id BIGINT UNSIGNED NOT NULL,
    nome VARCHAR(100) NOT NULL,
    simbolo VARCHAR(20) NOT NULL,
    casas_decimais TINYINT UNSIGNED NOT NULL DEFAULT 8,
    fornecimento_maximo DECIMAL(38, 18),
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uk_criptomoeda_simbolo
        UNIQUE (simbolo),

    CONSTRAINT fk_criptomoeda_blockchain
        FOREIGN KEY (blockchain_id)
        REFERENCES blockchain(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- =========================================
-- TABELA: TOKEN
-- =========================================
CREATE TABLE token (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    blockchain_id BIGINT UNSIGNED NOT NULL,
    nome VARCHAR(100) NOT NULL,
    simbolo VARCHAR(20) NOT NULL,
    endereco_contrato VARCHAR(255) NOT NULL,
    padrao VARCHAR(50),
    casas_decimais TINYINT UNSIGNED NOT NULL DEFAULT 18,
    fornecimento_total DECIMAL(38, 18),
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uk_token_contrato
        UNIQUE (blockchain_id, endereco_contrato),

    CONSTRAINT fk_token_blockchain
        FOREIGN KEY (blockchain_id)
        REFERENCES blockchain(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);