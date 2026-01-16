import pandas as pd

# Write a function to change the data type of given a column or a Series.
# Function takes series and data type as input, returns the converted series.

series = pd.Series([1,2,'Python', 2.0, True, 100])

def changeDataType(series):
    return pd.to_numeric(series, errors='coerce')
print(changeDataType(series))