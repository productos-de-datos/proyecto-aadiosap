"""
Módulo de creación de graficos de datos promedios diarios.
-------------------------------------------------------------------------------
En este modulo se genera una grafica para los precios promedios diarios, según 
los indices que sean elegistos en reset_index y el color y nombre que se
determinen en set_plot.

"""

"""Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.
"""
import pandas as pd
import matplotlib.pyplot as plt

def make_daily_prices_plot():
    path_to_save='data_lake/business/reports/figures/daily_prices.png'
    daily_princes = pd.read_csv('data_lake/business/precios-diarios.csv')
    figure_to_plot = reset_index(daily_princes,'Fecha','Price ($/kWh)')
    figure_to_plot = set_plot(figure_to_plot)
    save_fig(path_to_save)
    #raise NotImplementedError("Implementar esta función")

def reset_index(data,x_axis,y_axis):
    data.columns = [x_axis,y_axis]
    return data

def set_plot(figure_to_plot):
    color = 'Magenta'
    x = 'Fecha'
    return figure_to_plot.plot(x,color=color)

def save_fig(path_to_save):
    plt.savefig('data_lake/business/reports/figures/daily_prices.png')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    make_daily_prices_plot()