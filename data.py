import pandas 
from sklearn import linear_model 

def predict(x: str,y: str,c: str, day: str):
    df = pandas.read_csv(x)
    depented = df[[c]]
    independent = df[[y]]
    linear = linear_model.LinearRegression()
    linear.fit(depented, independent)
    global cases_predict 
    cases_predict  = linear.predict([[day]])
    print(cases_predict)

us = predict("us.csv", "cases", "Day", "15")
us_cases = int(cases_predict)
sa = predict("SA.csv", "cases", "Day", "16")
sa_cases = int(cases_predict)
uk = predict("uk.csv", "cases", "Day", "16")
uk_cases = int(cases_predict)

us_next = predict("us.csv", "cases", "Day", "23")
us_next_week = int(cases_predict)

sa_next = predict("SA.csv", "cases", "Day", "23")
sa_next_week = int(cases_predict)

uk_next = predict("uk.csv", "cases", "Day", "23")
uk_next_week =int(cases_predict)
