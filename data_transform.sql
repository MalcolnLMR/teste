-- Table Headers from statement 3.1 
-- "DATA";"REG_ANS";"CD_CONTA_CONTABIL";"DESCRICAO";"VL_SALDO_INICIAL";"VL_SALDO_FINAL"

CREATE DATABASE IF NOT EXISTS teste_de_nivelamento;

CREATE TABLE IF NOT EXISTS teste_de_nivelamento.demonstracoes_contabeis_de_2023_ate_2024 (
    DATA DATE,
    REG_ANS VARCHAR(255),
    CD_CONTA_CONTABIL VARCHAR(255),
    DESCRICAO VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(16,2),
    VL_SALDO_FINAL DECIMAL(16,2)
);

LOAD DATA LOCAL INFILE '/home/malcolnlmr/git/teste-de-nivelamento/data_sample/merged_data.csv'
INTO TABLE teste_de_nivelamento.demonstracoes_contabeis_de_2023_ate_2024
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
IGNORE 1 ROWS;


-- Table Headers from statement 3.2
-- Registro_ANS;CNPJ;Razao_Social;Nome_Fantasia;Modalidade;Logradouro;Numero;Complemento;Bairro;Cidade;UF;CEP;DDD;Telefone;Fax;Endereco_eletronico;Representante;Cargo_Representante;Regiao_de_Comercializacao;Data_Registro_ANS

CREATE TABLE IF NOT EXISTS teste_de_nivelamento.relatorio_cadop (
    REG_ANS VARCHAR(255),
    CNPJ VARCHAR(255),
    RAZAO_SOCIAL VARCHAR(255),
    NOME_FANTASIA VARCHAR(255),
    MODALIDADE VARCHAR(255),
    LOGRADOURO VARCHAR(255),
    NUMERO VARCHAR(255),
    COMPLEMENTO VARCHAR(255),
    BAIRRO VARCHAR(255),
    CIDADE VARCHAR(255),
    UF VARCHAR(255),
    CEP VARCHAR(255),
    DDD VARCHAR(255),
    TELEFONE VARCHAR(255),
    FAX VARCHAR(255),
    ENDERECO_ELETRONICO VARCHAR(255),
    REPRESENTANTE VARCHAR(255),
    CARGO_REPRESENTANTE VARCHAR(255),
    REGIAO_DE_COMERCIALIZACAO VARCHAR(255),
    DATA_REGISTRO_ANS DATE
);

LOAD DATA LOCAL INFILE '/home/malcolnlmr/git/teste-de-nivelamento/data_sample/Relatorio_cadop.csv'
INTO TABLE teste_de_nivelamento.relatorio_cadop
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
IGNORE 1 ROWS;