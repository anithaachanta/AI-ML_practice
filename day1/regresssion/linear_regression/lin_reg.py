from sklearn.linear_model import LinearRegression

x=[[2],[4],[6],[8],[10]]
y=[40,50,60,70,80]
model=LinearRegression()

model.fit(x,y)

predicition=model.predict([[7]])
print(predicition)