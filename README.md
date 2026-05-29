# 📊 Dashboard Executivo: Risco de Crédito e Prevenção de Churn

## 📌 Contexto e Problema de Negócio
No cenário financeiro, a retenção de clientes e a mitigação de inadimplência são pilares essenciais. Este projeto foi desenvolvido para analisar uma base de dados de cartões de crédito e atuar em duas frentes:
1. **Prevenção de Churn:** Identificar clientes com alta probabilidade de cancelamento com base em inatividade e uso do limite.
2. **Análise de Risco:** Avaliar o perfil de crédito da carteira ativa para prever potenciais inadimplências, segmentando por faixas salariais e estado civil.

## ⚙️ Arquitetura da Solução e Pipeline de Dados

O projeto foi dividido em três etapas claras, do dado bruto até a visualização final:

### 1. Extração e Tratamento (Python / Pandas)
**Arquivo:** `etl_tratamento.py`
* **Limpeza (Data Cleaning):** Identificação e tratamento de valores nulos nas colunas de `escolaridade`, `estado_civil` e `salario_anual`. Padronização de strings para evitar erros de agrupamento.
* **Feature Engineering:** * Criação da métrica `taxa_uso_credito` (percentual do limite utilizado).
  * Criação da flag `alerta_churn` (regra de negócio: clientes inativos há 3+ meses e com uso de limite inferior a 20% são classificados como "Risco Alto").

### 2. Validação e Consultas Avançadas (SQL)
**Arquivo:** `consultas_churn.sql`
* **CTEs (Common Table Expressions):** Utilizadas para isolar a base de clientes em risco e calcular métricas financeiras diretamente no banco.
* **Window Functions:** * Uso de `AVG() OVER (PARTITION BY)` para comparar a taxa de uso de um cliente com a média da sua faixa salarial.
  * Uso de `RANK() OVER (PARTITION BY)` para elencar os maiores gastadores dentro de cada estado civil.

### 3. Modelagem e Visualização (Power BI)
**Arquivo:** `Análise Credito.pbix`
* Importação da base tratada (`base_credito_tratada.csv`).
* Modelagem de dados focada em performance.
* Criação de medidas em **DAX** para consolidação de KPIs visuais (Taxa de Churn, Volume em Risco, Perfil de Inadimplência).

## 🚀 Como navegar neste repositório
- Os scripts de preparação e regras de negócio estão soltos na raiz do repositório (`.py` e `.sql`) para fácil leitura da lógica aplicada.
- A visualização final pode ser conferida na imagem abaixo ou baixando o arquivo `.pbix` para interação no Power BI Desktop.

[<img width="1493" height="838" alt="Churn1" src="https://github.com/user-attachments/assets/3ab44517-bd65-4b5f-a31d-df2f3313975b" />
]

---
**Desenvolvido por:** Igor Carvalho de Souza
*Graduação em Análise e Desenvolvimento de Sistemas - Universidade São Francisco (USF)*
