"""
Módulo de calculo de precios diarios.
-------------------------------------------------------------------------------
En este modulo se calculan los precios promedios diarios mediante la funcion 
groupby aplicado sobre la fecha YYYY-MM-DD.

"""

"""Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



"""

import pandas as pd
import doctest

def compute_daily_prices():
    prices_per_hour = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    prices_per_day = prices_per_hour.groupby('fecha').mean('precio')
    prices_per_day.to_csv('data_lake/business/precios-diarios.csv')
    print(prices_per_day.head())

#raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    doctest.testmod()
    compute_daily_prices()