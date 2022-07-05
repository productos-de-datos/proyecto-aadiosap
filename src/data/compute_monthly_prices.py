"""
Módulo de calculo de precios mensuales.
-------------------------------------------------------------------------------
En este modulo se calculan los precios promedios mensuales mediante la funcion 
groupby aplicado sobre la fecha YYYY-MM.

"""

"""Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



"""
import pandas as pd
import datetime as dt
import doctest

def compute_monthly_prices():
    #raise NotImplementedError("Implementar esta función")
    prices_per_hour = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    prices_per_month = prices_per_hour.copy()
    prices_per_month['fecha'] = prices_per_month['fecha'].map(lambda x:str(x)[0:7]+str('-01'))
    prices_per_month = prices_per_month.groupby('fecha').mean('precio')
    prices_per_month.to_csv('data_lake/business/precios-mensuales.csv')
    print(prices_per_month.head(25))


if __name__ == "__main__":
    doctest.testmod()
    compute_monthly_prices()