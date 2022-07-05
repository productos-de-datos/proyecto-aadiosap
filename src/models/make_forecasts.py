"""
Módulo de pronostico de datos.
-------------------------------------------------------------------------------
En este modulo se genera una copia del features para proceder a realizar
el pronostico de los datos utilizando el modelo precios-diarios.pkl
siendo casteado mediante la función pickle.load.

""""""Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


"""
import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split

def make_forecasts():
    features_data= pd.read_csv('data_lake/business/features/precios_diarios.csv')
    data_to_forecast = features_data.copy()
    data_to_forecast['day_number'] = pd.to_numeric(features_data['day_number'])

    X = np.array(data_to_forecast['day_number']).reshape(-1,1)
    
    with open('src/models/precios-diarios.pkl', 'rb') as f:
        estimator = pickle.load(f)
    
    data_to_forecast['forecasted'] = estimator.predict(X)
    data_to_forecast.to_csv('data_lake/business/forecasts/precios-diarios.csv',index=False)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    make_forecasts()
