CREATE DATABASE IF NOT EXISTS teste_de_nivelamento;

CREATE TABLE IF NOT EXISTS teste_de_nivelamento.demonstracoes_contabeis_de_2023_ate_2024 (
    DATA DATE,
    REG_ANS VARCHAR(255),
    CD_CONTA_CONTABIL VARCHAR(255),
    DESCRICAO VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(16,2),
    VL_SALDO_FINAL DECIMAL(16,2)
);

-- É um caminho absoluto.
LOAD DATA LOCAL INFILE '/home/malcolnlmr/git/teste-de-nivelamento/data_sample/merged_data.csv'
INTO TABLE teste_de_nivelamento.demonstracoes_contabeis_de_2023_ate_2024
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
IGNORE 1 ROWS;