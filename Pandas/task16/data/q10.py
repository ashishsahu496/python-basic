import pandas as pd

# i. Find mean price
# ii. Find 30th and 6th percentile value
# iii. Plot Histogram on price with bin size 50
# iv. No of items price lies between [1000 to 2000]

itm=pd.read_csv("C:/DSMP/Python/Pandas/task16/data/items.csv",index_col=['item_name']).squeeze("columns")
# # print(itm)
# def rupees(x):
#     try:
#         y=x[1:]
#     except:
#         y=x
#     return float(y)*91
#
# print(itm.apply(rupees))
#
# # print("item_price ka mean",itm['item_price'].mean())
# print(itm.describe())
# print(itm.quantile(q=0.3))

# print(itm.mean())
itm.plot.hist(bins=50)