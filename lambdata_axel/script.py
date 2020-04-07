import pandas as pd
from lambdata_axel.ds_tools import check_nulls_df, train_val_test_split

df = pd.DataFrame({'numbers': [0,1,2,3,4,5,6,7],"alphabet": ['a','b','c','d','e','f','g','h']})

check_nulls_df(df)

train, val, test = train_val_test_split(df,24)
print(train)
print(val)
print(test)