from datetime import date
from pandas import concat


def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import pandas as pd
    import os
    
    files_to_combine = os.listdir('data_lake/raw')
    files_to_combine = list(map(lambda x:'data_lake/raw/'+str(x),files_to_combine))
    dataFrame = pd.concat(map(pd.read_csv,files_to_combine), ignore_index=True)
    dataFrame = pd.melt(dataFrame,id_vars=['Fecha'])
    dataFrame.to_csv('data_lake/cleansed/precios-horarios.csv',index=False)




#    raise NotImplementedError("Implementar esta función")




if __name__ == "__main__":
    import doctest

    doctest.testmod()

clean_data()