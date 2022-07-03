def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    #raise NotImplementedError("Implementar esta función")
    import pandas as pd
    import datetime as dt

    prices_per_hour = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    prices_per_month = prices_per_hour.copy()
    prices_per_month['month'] = prices_per_month['Fecha'].map(lambda x:str(x)[0:7]+str('-01'))
    prices_per_month = prices_per_month.groupby('month').mean('Value')
    #prices_per_month.to_csv('data_lake/business/precios-diarios.csv')
    print(prices_per_month.head(25))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

compute_monthly_prices()