Ecommerce Data Pipeline

Projeto de pipeline de dados desenvolvido com foco em **ETL (Extração, Transformação e Carga)** usando Python e boas práticas de organização de código.

## Objetivo

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
- VScode

Como usar

1. Clone o repositório:
 
 git clone https://github.com/gustavogchiavarini/ecommerce-data-pipeline.git
Instale as dependências:
pip install -r requirements.txt

Execute o pipeline:
python src/pipeline.py

Etapas do Pipeline

Extração dos dados de ecommerce (pode ser de um arquivo .csv)
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

