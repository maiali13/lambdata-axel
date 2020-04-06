import pandas as pd

def check_nulls_df(df):
  result = df.isnull().sum()
  print(result)