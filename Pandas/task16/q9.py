import pandas as pd
import numpy as np

#i. Read `items.csv` making `item_name` as index.
# ii. Show no of nan values
# ii. Item price is given in $, so convert it to rupees without currency symbol.
# iii. Make data type of newly made series as float.
# iv. Fill nan with mean of the series

itm=pd.read_csv("C:/DSMP/Python/Pandas/task16/data/items.csv",index_col=['item_name']).squeeze("columns")
# print(itm)
# print(itm.isna().sum())

def rupees(x):
    try:
        y=x[1:]
    except:
        y=x
    return float(y)*91

# print(itm.apply(rupees))
itm.fillna(itm.mean())
# print(itm.isna().sum())

