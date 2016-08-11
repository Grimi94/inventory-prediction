import pandas as pd
def read_data(path):
    df = pd.read_csv(path, parse_dates=['FECHA'], infer_datetime_format=True)
    df['CPRECIO'] = df[' CPRECIO '].map(lambda x: x.strip().replace(",", ""))
    df['CPRECIO'] = df['CPRECIO'].convert_objects(convert_numeric=True)
    df['COSTOPESOS'] = df[' COSTOPESOS ']
    df = df.drop([' CPRECIO ', ' COSTOPESOS '], axis=1)
    cols = df.columns.values
    cols[-3] = "YEAR"
    df.columns = cols
    return df

def clean_data(df):
    # Cleanup all the spaces
    df["MARCA"] = df["MARCA"].map(lambda x: x.strip())
    df["IDPRODUCTO"] = df["IDPRODUCTO"].map(lambda x: x.strip())
    return df

def load_data(path):
    df = read_data(path)
    return clean_data(df)
