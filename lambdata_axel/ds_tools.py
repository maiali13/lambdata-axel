import pandas as pd
from sklearn.model_selection import train_test_split

def check_nulls_df(df):
  """
  param df is a pandas dataframe

  will check if it contains any nulls
  """
  result = df.isnull().sum()
  print(result)

def train_val_test_split(df,random_state):
  """
  param df is a pandas dataframe
  param random_state will be used in sklearn function

  function will split the dataframe into train, val, test set
  """
  train, test = train_test_split(df,random_state=random_state)
  train, val = train_test_split(train,random_state=random_state)
  return train, val, test