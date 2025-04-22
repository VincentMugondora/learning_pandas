import pandas as pd

# Series is a one-dimensional labeled array that can hold any type of data—integers, floats, strings, or even Python objects
# It is similar to a list or a dictionary, but with additional features like indexing and alignment.
# It is a fundamental building block of pandas and is used to represent a single column of data in a DataFrame.

# Creating a Series from a list
data = [10, 20, 30, 40]
series = pd.Series(data)

print(series)

series = pd.Series(data, index=["A", "B", "C", "D"])
print(series)