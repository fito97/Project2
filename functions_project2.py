import pandas as pd

def read_clean_file(path):
        df = pd.read_excel(path)
        df.drop(columns=["Country Name","Country Code"],inplace=True)
        df1 = df.transpose().reset_index()
        transposed_columns = df1.loc[0]
        df1.columns =transposed_columns
        df1.drop(0,inplace=True)
        df1.replace("..",0,inplace=True)
        df1.fillna(0,inplace=True)

        return df1


def date_clean_up(df):
      df['Series Name'] = df['Series Name'].str.replace(r'\[.*?\]', '', regex=True).str.strip()
      df['Series Name'] = pd.to_numeric(df['Series Name'])