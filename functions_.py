import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def model(x_train, x_test, y_train, y_test):
    linreg = LinearRegression()
    linreg.fit(x_train, y_train)
    y_hat_train = linreg.predict(x_train)
    y_hat_test = linreg.predict(x_test)
    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)
    print('Train Mean Square Error:', train_mse)
    print('Test Mean Square Error:', test_mse)
    print('Train Root Mean Square Error:', train_mse**0.5)
    print('Test Root Mean Square Error:', test_mse**0.5)
    
    df = y_train.join(x_train)
    f = 'quality ~ '+ ' + '.join(x_train.columns)
    model = ols(formula=f, data=df).fit()
    return model.summary()