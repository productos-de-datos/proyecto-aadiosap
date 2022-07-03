"""
Módulo de entrenamiento de modelo de pronostico de precios futuros.
-------------------------------------------------------------------------------

"""


def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    def set_data(path):
        data_to_train = pd.read_csv('data_lake/business/features/precios_diarios.csv')
        return data_to_train

    def format_dates(data):
        data['Fecha'] = data['Fecha'].apply(
                lambda x: datetime.strptime(x,"%Y-%m-%d") if type(x) == str else x)
        return data
        
    from sklearn import linear_model
    import pandas as pd
    from datetime import datetime

    regr = linear_model.LinearRegression()

    data_to_train = set_data(path)
    data_to_train = format_dates(data_to_train)
    print(data_to_train.dtypes)
    x = data_to_train.Fecha
    y = data_to_train.value
    regr.fit(x, y)
    print("Coeficientes: ", regr.coef_)
    print("\nIntercepto: ", regr.intercept_)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    path = 'data_lake/business/features/precios_diarios.csv'
    doctest.testmod()
    train_daily_model()
