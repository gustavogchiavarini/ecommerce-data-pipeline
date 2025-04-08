import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=["InvoiceDate"])
    print(f"Arquivo carregado com sucesso. Total de linhas: {len(df)}")
    return df

if __name__ == "__main__":
    path = "data/processed/ecommerce_tratado.csv"
    df = load_data(path)
    print(df.dtypes)
    print(df.head())
