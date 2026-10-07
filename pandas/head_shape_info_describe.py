import pandas as pd

data={
    "Name":["Ani","surya","varshi"],
    "Age":[22,28,21],
    "Score":[85,85,90]
}

df=pd.DataFrame(data)
"""
print(df)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
"""
#print(df[["Age","Score"]])
x=df[["Age"]]
y=df["Score"]

print(x)
print(y)
print(x.shape)
print(y.shape)