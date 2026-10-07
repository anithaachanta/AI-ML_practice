import pandas as pd

df=pd.read_csv("student.csv")

print(df)

x=df[["Hours_Studied"]]
     
y=df["Score"]

print("x:")
print(x)

print("y:")
print(y)

print(x.shape)
print(y.shape)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train:")
print(x_train)

print("X_test:")
print(x_test)

print("y_train:")
print(y_train)

print("y_test:")
print(y_test)