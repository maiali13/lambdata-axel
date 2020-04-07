import pandas as pd
from lambdata_axel.ds_tools import DSDataFrameTools


df = pd.DataFrame({'numbers': [0, 1, 2, 3, 4, 5, 6, 7], "alphabet": [
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']})

DSDataFrameTools(df).check_nulls_df()

train, val, test = DSDataFrameTools(df).train_val_test_split(random_state=24)
print(train)
print(val)
print(test)
