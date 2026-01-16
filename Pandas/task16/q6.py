import pandas as pd
# Find top 10 most run getter from the series.
# No of players having runs above 3000
# No of players having runs above mean value?

n1=pd.read_csv("C:/DSMP/Python/Pandas/task16/data/batsman_runs_series.csv")
# print(n1)
# print(n1.sort_values('batsman_run',ascending=False).head(10))
# print(n1[n1["batsman_run"]>3000].shape[0])
print(n1[n1['batsman_run'] > n1['batsman_run'].mean()].shape[0] )
# print(n1['batsman_run'].std())
# print(n1.describe())