import pandas as pd
from sklearn.model_selection import train_test_split


class DSDataFrameTools():
    """
    Params:
    df: uses a pandas dataframe
    """

    def __init__(self, df):
        self.df = df

    def check_nulls_df(self):
        """
        will check if it contains any nulls
        """
        result = self.df.isnull().sum()
        print(result)

    def train_val_test_split(self, random_state):
        """
        param random_state will be used in sklearn function

        function will split the dataframe into train, val, test set
        """
        train, test = train_test_split(self.df, random_state=random_state)
        train, val = train_test_split(train, random_state=random_state)
        return train, val, test
