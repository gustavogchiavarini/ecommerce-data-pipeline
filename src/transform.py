import pandas as pd
from extract import extract_data

def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.dropna(subset=["CustomerID","Description"]).copy()

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    df = df[(df["Quantity"] > 0 ) & (df["UnitPrice"] > 0)].copy()

    df = df.drop_duplicates().copy()

    print(f"Transformação concluída. Total de linhas após a limpeza:  {len(df)}")
    return df 

if __name__ == "__main__":
    path = "data/raw/ecommerce_sales.csv"
    df_raw = extract_data(path)
    df_clean = clean_data(df_raw)
    print (df_clean.head())

    df_clean.to_csv("data/processed/ecommerce_tratado.csv", index=False)
