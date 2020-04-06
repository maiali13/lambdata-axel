import pandas as pd
from lambdata_axel.ds_tools import check_nulls_df

df = pd.DataFrame({'numbers': [0,1,2,3,4]})

check_nulls_df(df)