# multiple regression is like linear regression but with more than one independent value

import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")
x = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x, y)

# example
# predict the CO2 emission of car where the weight is 2300 kg and the volume is 1300 cm3
predictedCO2 = regr.predict([[2300, 1300]])

# we have predicted that a car with 1.3 litre engine and a weight of 2300 kg will release approximately 107 grams of CO2 for every kilometre it drives
print(predictedCO2)

# print the coefficient values of the regression object
print(regr.coef_)
# represents the coefficient values of weight and volume
# weight : 0.00755095 g
# these values tell us that if the weight increase by 1 kg
# the CO2 emmision increases by 
# volume : 0.00780526 g
# and if the engine size (volume) increases by 1 cm3
# the CO2 emission increases by