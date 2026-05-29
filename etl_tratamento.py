import pandas as pd
import numpy as np

# Carregando a base de dados original
print("Lendo o arquivo csv...")
base = pd.read_csv('credito.csv')
# print(base.shape) # deixei comentado pra não sujar o terminal depois

# Tratando os valores nulos 
# Notei que tinha bastante coisa vazia na escolaridade e estado civil
colunas_vazias = ['escolaridade', 'estado_civil', 'salario_anual']
for col in colunas_vazias:
    base[col].fillna('Não Informado', inplace=True)
    
# Padronizando o texto pra evitar erro de agrupamento no Power BI depois
base['estado_civil'] = base['estado_civil'].str.upper()
base['escolaridade'] = base['escolaridade'].str.upper()

# Feature Engineering (criando métricas novas)
# 1. Taxa de uso do limite (gasto total / limite disponível)
base['taxa_uso_credito'] = np.where(
    base['limite_credito'] > 0, 
    base['valor_transacoes_12m'] / base['limite_credito'], 
    0
)

# 2. Segmentação de risco 
# Regra de negócio: se o cliente tá inativo faz 3 meses e usa pouco o limite, o risco de churn é alto
base['alerta_churn'] = np.where(
    (base['meses_inativo_12m'] >= 3) & (base['taxa_uso_credito'] < 0.2), 
    'Risco Alto', 
    'Normal'
)

# Exportando a base limpa pra conectar direto no Power BI
base.to_csv('base_credito_tratada.csv', index=False)
print("Tratamento finalizado! Base salva com sucesso.")
