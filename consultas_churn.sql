-- Consulta para separar os clientes com risco de churn e comparar perfis
-- Usando CTE pra facilitar a leitura da query principal

WITH base_risco AS (
    SELECT 
        id,
        idade,
        salario_anual,
        limite_credito,
        valor_transacoes_12m,
        inadimplente,
        meses_inativo_12m,
        -- calculando a taxa de uso do cartao direto no banco
        (valor_transacoes_12m / NULLIF(limite_credito, 0)) AS tx_uso
    FROM 
        tb_clientes_credito
    WHERE 
        meses_inativo_12m >= 2
)

SELECT 
    r.id,
    r.idade,
    r.salario_anual,
    r.inadimplente,
    r.tx_uso,
    
    -- Trazendo a média de uso de acordo com a faixa salarial da pessoa (Window Function)
    AVG(r.tx_uso) OVER (PARTITION BY r.salario_anual) AS media_uso_faixa,
    
    -- Rankeando os maiores gastadores dentro do mesmo estado civil
    RANK() OVER (PARTITION BY c.estado_civil ORDER BY r.valor_transacoes_12m DESC) as rank_gasto
    
FROM 
    base_risco r
LEFT JOIN 
    tb_clientes_credito c ON r.id = c.id
WHERE 
    r.inadimplente = 'Sim'
ORDER BY 
    r.tx_uso DESC;
