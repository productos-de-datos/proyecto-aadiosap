"""
Módulo de entrenamiento de modelo de pronostico de precios futuros.
-------------------------------------------------------------------------------
Según la información guardada en make features se realiza un particionamiento
de los datos para entrenar el modelo de regresión linea. Luego de
hacer el entrenamiento este se guarda mediante la función pickle.dump
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import numpy as np
import pickle

def train_daily_model():

    df = pd.read_csv('data_lake/business/features/precios_diarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    df['day_number'] = pd.to_numeric(df['day_number'])

    X = np.array(df['day_number']).reshape(-1, 1)
    y = np.array(df['precio']).reshape(-1, 1)

    print(X)
    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=22)
    regr = linear_model.LinearRegression()
    model = regr.fit(X_train, y_train)
    pickle.dump(model, open("src/models/precios-diarios.pkl", "wb"))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    train_daily_model()
