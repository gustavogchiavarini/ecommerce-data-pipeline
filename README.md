Ecommerce Data Pipeline

Este projeto é uma simulação de um pipeline de dados para um ecommerce. Ele representa um fluxo de extração, transformação e carregamento (ETL) de dados brutos até um formato pronto para análise.

Objetivo

Demonstrar, na prática, as principais etapas de um pipeline de dados com foco em:

- Organização de projeto
- Boas práticas com Git
- ETL com Python
- Armazenamento em CSV/Parquet
- Preparação para análise

Tecnologias e Ferramentas

- Python 
- Pandas
- Git & GitHub

Como usar

1. Clone o repositório:
 
 git clone https://github.com/gustavogchiavarini/ecommerce-data-pipeline.git
Instale as dependências:
pip install -r requirements.txt

Execute o pipeline:

bash
Copiar
Editar
python src/pipeline.py

Etapas do Pipeline

Extração dos dados fictícios de ecommerce (pode ser de um arquivo .csv)
Transformação para limpar, filtrar e enriquecer os dados
Carga dos dados em um novo arquivo .csv pronto para análise

Exemplos de Análise (futuro)

Ticket médio por cliente
Produtos mais vendidos
Receita por mês
Top regiões de venda

Próximos passos
Armazenamento em banco de dados (PostgreSQL, SQLite, etc.)
Automatização do pipeline (Airflow, Prefect, etc.)
Dashboard com Power BI / Streamlit

