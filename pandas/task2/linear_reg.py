import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("student.csv")

X = df[["Hours_Studied"]]
y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)
#evalution metrics
print("Slope:", model.coef_)
print("Intercept:", model.intercept_)
print("R^2:",model.score(X_test,y_test))

y_pred = model.predict(X_test)

print("Actual:", y_test.values)
print("Predicted:", y_pred)