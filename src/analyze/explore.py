import pandas as pd

def explore_data(df: pd.DataFrame):
    print("Informações básicas do DataFrame:")
    print(df.info())
    
    print("Estatísticas descritivas:")
    print(df.describe())

    print("Valores únicos por coluna:")
    print(df.nunique())

    print("Valores nulos restantes:")
    print(df.isnull().sum())

    print("Países com mais compras:")
    print(df["Country"].value_counts().head(10))

if __name__ == "__main__":
    path = "data/processed/ecommerce_tratado.csv"
    df = pd.read_csv(path)

    explore_data(df)
