import pandas as pd
import numpy as np

# Pandas is a Python module for working with tabular data (i.e., data in a table with rows and columns). Tabular data has a lot of the same functionality as SQL or Excel, but Pandas adds the power of Python.

l1 = [2,5,4,7,8,9] # list

d1 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]} # rename index

for i in enumerate(l1):
    print(i)


# Creating a Pandas Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

# Displaying the Series
print("Pandas Series:")
print(series)

# Accessing an element using its index
print("\nAccessing element with index 'c':")
print(series['c'])


print(pd.Series(l1))

s1 = pd.Series((3,4,5),index=["a", 'b', 'c'])
print(s1)