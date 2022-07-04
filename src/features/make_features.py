"""
Módulo de caracteristicas del modelo de proponistuco de precios.
-------------------------------------------------------------------------------

"""

"""Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
import pandas as pd
def make_features():
    df = pd.read_csv('data_lake/business/precios-diarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    df['day_number'] = df.fecha.dt.weekday
    df.to_csv('data_lake/business/features/precios_diarios.csv', index=False)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    make_features()
