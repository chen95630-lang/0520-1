import pandas as pd

data_dict = {
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"],
    "Price": [30, 20, 25, 60, 45, 35],
    "Sales": [100, 150, 80, 60, 90, 54]
}

df1 = pd.DataFrame(data_dict)

print(df1.head())
print(df1.tail())

data_list = [
    ["Apple", 30, 100],
    ["Banana", 20, 150],
    ["Orange", 25, 80],
    ["Mango", 60, 60],
    ["Grape", 45, 90],
    ["Guava", 35, 54]
]

df2 = pd.DataFrame(data_list, columns=["Product", "Price", "Sales"])

print(df2.shape)

print(df2.columns)

print(df2.dtypes)

print(df2.count())

stats = df2.describe().round(2)

print(stats)

stats.to_csv("0520_stock2.csv")