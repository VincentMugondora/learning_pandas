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

# series using tuples
t1 = (3,4,5)
s1 = pd.Series((3,4,5),index=["a", 'b', 'c'])
print(s1)

dt = {"a": 3, "b": 4, "c": 5}

# series using lists
l1 = [3, 'hello', 5, 56, 'hi']
s2 = pd.Series(l1, index=["a", 'b', 'c', 'd', 'e'])
print(s2)


t1 = pd.Series([3, 4, 5], index=["a", 'b', 'c'])
t2 = pd.Series([3, 5, 8], index=["a", 'b', 'c'])
print(t1 + t2) # addition of two series


# position based indexing
print(t1[0]) # first element
print(t1[1]) # second element

# label based indexing
print(t1['a']) # first element
print(t1['b']) # second element

# range
print(s2)
print(s2[0:3]) # first three elements, last range is excluded in position based indexing
print(s2[1:4]) # second to fourth elements

print(s2['a':'d']) # last range is included in label based indexing

print(s2[['a', 'c', 'e']]) # accessing multiple elements using label based indexing