import pandas
from sklearn import linear_model

df_cars = pandas.read_csv('cars.csv')

X = df_cars[['Volume', 'Weight']]
y = df_cars['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

co2 = regr.predict([[3200, 2500]])

print(co2)

