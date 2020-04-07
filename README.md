# lambdata-axel

## installation

```python
pip install -i https://test.pypi.org/simple/ lambdata-axel
```

## usage

import

```python
from lambdata_axel.ds_tools import check_nulls_df, train_val_test_split
```

check for nulls in a dataframe

```python
check_nulls_df(df)
```

create a train, validate, and test set from a dataframe

```python
train, val, test = train_val_test_split(df,24)
```
