import pandas as pd
import os


'''
Lê um arquivo CSV e retorna um DataFrame.
Parâmentros: filepath(str) : Caminho do arquivo.
Retorno: pd.DataFrame, Dados carregados.
'''
def extract_data(filepath: str) -> pd.DataFrame:
    if not os.path.exists(filepath):
        raise  FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    
    df = pd.read_csv(filepath, encoding='latin1')
    print(f"Dados carregados com sucesso. Total de linhas:{len(df)}")
    return df

if __name__=="__main__":
    path = "data/raw/ecommerce_sales.csv"
    df = extract_data(path)
    print(df.head())

