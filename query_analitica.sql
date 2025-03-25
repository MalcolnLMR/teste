SELECT 
    cadop.RAZAO_SOCIAL AS Razao_Social,
    cadop.NOME_FANTASIA AS Nome_Fantasia,
    SUM(dc.VL_SALDO_FINAL - dc.VL_SALDO_INICIAL) AS Total_Despesas
FROM 
    teste_de_nivelamento.demonstracoes_contabeis_de_2023_ate_2024 dc
JOIN 
    teste_de_nivelamento.relatorio_cadop cadop
ON 
    dc.REG_ANS = cadop.REG_ANS
WHERE 
    dc.DESCRICAO = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
    AND MONTH(dc.DATA) = 10
    AND YEAR(dc.DATA) = 2024
GROUP BY 
    cadop.NOME_FANTASIA
ORDER BY 
    Total_Despesas DESC
LIMIT 10;

SELECT 
    cadop.RAZAO_SOCIAL AS Razao_Social,
    cadop.NOME_FANTASIA AS Nome_Fantasia,
    SUM(dc.VL_SALDO_FINAL - dc.VL_SALDO_INICIAL) AS Total_Despesas
FROM 
    teste_de_nivelamento.demonstracoes_contabeis_de_2023_ate_2024 dc
JOIN 
    teste_de_nivelamento.relatorio_cadop cadop
ON 
    dc.REG_ANS = cadop.REG_ANS
WHERE 
    dc.DESCRICAO = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
    AND YEAR(dc.DATA) = 2024
GROUP BY 
    cadop.NOME_FANTASIA
ORDER BY 
    Total_Despesas DESC
LIMIT 10;