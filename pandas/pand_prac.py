import pandas as pd

data={
    "Name":["Anitha","Surya","Varshi"],
    "Age":[22,28,21],
    "Score":[85,83,90]
}

df=pd.DataFrame(data)
print(df)
print(df["Score"])